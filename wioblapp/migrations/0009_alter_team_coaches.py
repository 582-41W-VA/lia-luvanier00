# Generated by Django 5.1.5 on 2025-02-09 19:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0008_team_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="coaches",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="teams", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
