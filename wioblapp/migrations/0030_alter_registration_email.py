# Generated by Django 5.1.5 on 2025-02-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wioblapp', '0029_merge_20250220_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email Address'),
        ),
    ]
