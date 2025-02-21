# Generated by Django 5.1.5 on 2025-02-18 19:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0024_alter_comment_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="team1_score",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Team #1 Score",
            ),
        ),
        migrations.AlterField(
            model_name="game",
            name="team2_score",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Team #2 Score",
            ),
        ),
        migrations.AlterField(
            model_name="registrationtype",
            name="cost",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Cost",
            ),
        ),
        migrations.AlterField(
            model_name="team",
            name="place",
            field=models.IntegerField(
                default=0,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Place",
            ),
        ),
    ]
