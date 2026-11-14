from django.contrib.auth.models import AbstractUser
from django.db import models
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=20, blank=True)
    onboarded_at = models.DateTimeField(null=True, blank=True)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        self.email = self.email.strip().lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_full_name() or self.email
