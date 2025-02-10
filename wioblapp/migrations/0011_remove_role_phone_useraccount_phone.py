# Generated by Django 5.1.5 on 2025-02-10 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wioblapp', '0010_role_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='phone',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
    ]
