from django.db import models
from django.utils import timezone
from accounts.models import Account

class Transaction(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    amount = models.FloatField()
    type = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.account.user.username} - {self.type} - {self.amount}"
