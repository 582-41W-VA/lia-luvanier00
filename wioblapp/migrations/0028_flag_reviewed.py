# Generated by Django 5.1.5 on 2025-02-18 23:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0027_remove_useraccount_bio"),
    ]

    operations = [
        migrations.AddField(
            model_name="flag",
            name="reviewed",
            field=models.BooleanField(default=False),
        ),
    ]
