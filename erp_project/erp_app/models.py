from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ERPProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_date = models.DateField()
    exposure_text = models.TextField()
    response_prevention_text = models.TextField()
    completed = models.BooleanField(default=False)