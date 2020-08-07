from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.conf import settings



TIMEZONES_AMERICA = "America/Los_Angeles"
TIMEZONES_ASIA = "Asia/Kolkata"
TIMEZONES_CANADA = "Canada/Eastern"

TIMEZONES_CHOICES = (
    (TIMEZONES_AMERICA, TIMEZONES_AMERICA),
    (TIMEZONES_ASIA, TIMEZONES_ASIA),
    (TIMEZONES_CANADA, TIMEZONES_CANADA)
)

# Create your models here.


class User(AbstractUser):
    username = models.CharField(blank=True, null=True, max_length=50)
    real_name = models.CharField(max_length=50, unique=True)
    time_zone = models.CharField(max_length=100, blank=True, null=True, choices=TIMEZONES_CHOICES, default=TIMEZONES_ASIA)

    USERNAME_FIELD = 'real_name'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activityperiods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()