# Generated by Django 5.0.5 on 2024-05-29 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]