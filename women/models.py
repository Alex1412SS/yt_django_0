from django.db import models
from django.contrib.auth.models import User

class client(models.Model):
    title = models.CharField('Ваш телефон для связи', max_length=255)
    time_cre = models.DateTimeField(auto_now_add=True)
    time_upd = models.DateTimeField(auto_now=True)
    is_pub = models.BooleanField(default=True, db_index=True, verbose_name='Опубликовано', blank=False)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
