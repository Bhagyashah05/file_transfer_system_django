from rest_framework import serializers
from .models import File, TransferHistory

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'

class TransferHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransferHistory
        fields = '__all__'
