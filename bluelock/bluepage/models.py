from django.contrib.auth.models import User
from django.db import models

class Ai_tools(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=200)
    about = models.CharField(max_length=400)
    data_time = models.DateTimeField(blank=True)
    link_to = models.CharField(max_length=300)
    image = models.ImageField(blank=True, upload_to='Images')

    def __str__(self):
        return self.name