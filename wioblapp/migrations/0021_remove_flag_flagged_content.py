# Generated by Django 5.1.5 on 2025-02-16 21:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wioblapp', '0020_flag_flagged_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flag',
            name='flagged_content',
        ),
    ]
