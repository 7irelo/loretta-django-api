from django.db import models
from django.utils import timezone
from users.models import User

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=255)
    balance = models.FloatField()
    status = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.type}"
