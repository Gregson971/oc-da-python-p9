# Generated by Django 4.2.7 on 2023-12-11 22:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_auto_20231208_1350"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_photo",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Photo de profil"
            ),
        ),
    ]
