# Generated by Django 4.2.7 on 2023-12-08 12:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("reviews", "0002_alter_review_rating"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserFollows",
        ),
    ]
