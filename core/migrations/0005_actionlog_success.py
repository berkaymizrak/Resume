# Generated by Django 4.0.6 on 2024-04-15 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_actionlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='actionlog',
            name='success',
            field=models.BooleanField(default=True),
        ),
    ]
