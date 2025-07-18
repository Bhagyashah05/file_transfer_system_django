from django.urls import path
from .views import TransferFileView, RevokeFileView
from .views import TransferHistoryView
urlpatterns = [
    path('transfer/', TransferFileView.as_view(), name='transfer'),
    path('revoke/', RevokeFileView.as_view(), name='revoke'),
    path('history/<int:file_id>/', TransferHistoryView.as_view(), name='history'),
]
