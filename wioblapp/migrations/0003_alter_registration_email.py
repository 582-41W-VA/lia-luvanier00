# Generated by Django 5.1.5 on 2025-02-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("wioblapp", "0002_alter_useraccount_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registration",
            name="email",
            field=models.EmailField(
                blank=True, max_length=254, null=True, verbose_name="Email Adress"
            ),
        ),
    ]
