# Generated by Django 5.0.1 on 2024-04-06 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bluepage', '0002_ai_tools_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ai_tools',
            name='data_time',
            field=models.DateTimeField(blank=True),
        ),
    ]
