# Generated by Django 5.0.5 on 2024-07-26 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_notification_related_object_id'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('notification_type', 'related_object_id')},
        ),
    ]