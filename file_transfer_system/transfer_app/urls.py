from django.urls import path
from .views import TransferFileView, RevokeFileView

urlpatterns = [
    path('transfer/', TransferFileView.as_view(), name='transfer'),
    path('revoke/', RevokeFileView.as_view(), name='revoke'),
]
