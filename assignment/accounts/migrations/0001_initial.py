# Generated by Django 4.1.10 on 2023-09-02 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("name", models.CharField(max_length=200, unique=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=355)),
                ("verification_token", models.UUIDField(blank=True, null=True)),
                ("is_ops", models.BooleanField(default=False)),
                ("is_client", models.BooleanField(default=False)),
                ("is_verified", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
