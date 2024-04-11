from django.db import models
from django.contrib.auth.models import User
class profile_model(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(blank=True, upload_to='profile_images')

