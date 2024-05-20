# Generated by Django 5.0.5 on 2024-05-20 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_answer_created_at_alter_answer_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='rection',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rection_set', to='main.answer'),
        ),
        migrations.AlterField(
            model_name='rection',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]
