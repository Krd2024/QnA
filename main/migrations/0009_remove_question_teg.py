# Generated by Django 5.0.5 on 2024-06-06 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_question_tegs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='teg',
        ),
    ]
