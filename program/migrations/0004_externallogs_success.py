# Generated by Django 4.0.6 on 2023-05-06 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_externallogs'),
    ]

    operations = [
        migrations.AddField(
            model_name='externallogs',
            name='success',
            field=models.BooleanField(default=False, verbose_name='Success'),
        ),
    ]
