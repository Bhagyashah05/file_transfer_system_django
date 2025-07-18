from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_files')
    original_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='original_files')
    created_at = models.DateTimeField(auto_now_add=True)

class TransferHistory(models.Model):
    ACTIONS = (('TRANSFER', 'Transfer'), ('REVOKE', 'Revoke'))

    file = models.ForeignKey(File, on_delete=models.CASCADE)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_made')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transfers_received')
    action = models.CharField(max_length=10, choices=ACTIONS)
    timestamp = models.DateTimeField(auto_now_add=True)
