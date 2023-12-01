# Generated by Django 4.2.7 on 2023-11-30 22:01

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="follows",
            field=models.ManyToManyField(
                limit_choices_to={"role": "CREATOR"},
                to=settings.AUTH_USER_MODEL,
                verbose_name="suit",
            ),
        ),
    ]
