# Generated by Django 5.1.5 on 2025-02-16 21:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0019_remove_flag_flagged_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="flag",
            name="flagged_content",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Flagged Content"
            ),
        ),
    ]
