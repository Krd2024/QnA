# Generated by Django 5.0.5 on 2024-08-03 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_notification_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('notification_type', 'related_object_id', 'sender', 'recipient')},
        ),
    ]
