# Generated by Django 4.0.6 on 2024-04-16 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_coursecoupons_is_deleted_skill_is_deleted_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursecoupons',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='coursecoupons',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='skilltypes',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='skilltypes',
            old_name='updated_date',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='created_date',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='socialmedia',
            old_name='updated_date',
            new_name='updated_at',
        ),
    ]
