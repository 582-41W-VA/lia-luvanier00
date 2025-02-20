# Generated by Django 5.1.5 on 2025-02-09 18:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0007_remove_team_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="team",
            name="group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="teams",
                to="wioblapp.registrationtype",
            ),
        ),
    ]
