from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import File, TransferHistory
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from .serializers import TransferHistorySerializer
from rest_framework.permissions import IsAuthenticated

class TransferFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')
        to_user_id = request.data.get('to_user_id')
        try:
            file = File.objects.get(id=file_id)
            if file.owner != request.user:
                return Response({"error": "Not the current owner."}, status=403)

            to_user = User.objects.get(id=to_user_id)
            file.owner = to_user
            file.save()
            TransferHistory.objects.create(
                file=file, from_user=request.user, to_user=to_user,
                action='TRANSFER'
            )
            
            return Response({"message": "Ownership transferred."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

class RevokeFileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        file_id = request.data.get('file_id')
        try:
            file = File.objects.get(id=file_id)
            if file.original_owner != request.user:
                return Response({"error": "Only the original owner can revoke."}, status=403)

            TransferHistory.objects.create(
                file=file, from_user=file.owner, to_user=request.user,
                action='REVOKE'
            )
            file.owner = request.user
            file.save()
            return Response({"message": "Ownership revoked."}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=400)


class TransferHistoryView(ListAPIView):
    serializer_class = TransferHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        file_id = self.kwargs['file_id']
        return TransferHistory.objects.filter(file__id=file_id).order_by('-timestamp')