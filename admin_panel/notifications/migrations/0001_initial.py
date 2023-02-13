# Generated by Django 4.1.6 on 2023-02-13 07:11

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.SlugField(max_length=255, verbose_name="name")),
                (
                    "config_value",
                    models.CharField(max_length=255, verbose_name="value"),
                ),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Template",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "channel",
                    models.CharField(
                        choices=[("email", "Email"), ("websocket", "Websocket")],
                        max_length=50,
                    ),
                ),
                ("subject", models.TextField(blank=True, null=True)),
                ("template", tinymce.models.HTMLField()),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ScheduledMailing",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="description"),
                ),
                (
                    "template_params",
                    models.TextField(
                        blank=True, null=True, verbose_name="template_params"
                    ),
                ),
                (
                    "user_group",
                    models.CharField(choices=[("all", "All")], max_length=50),
                ),
                ("is_instant", models.BooleanField()),
                ("next_planned_date", models.DateTimeField(blank=True, null=True)),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("once", "Once"),
                            ("daily", "Daily"),
                            ("weekly", "Weekly"),
                            ("monthly", "Monthly"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "priority",
                    models.CharField(
                        choices=[("low", "Low"), ("high", "High")], max_length=50
                    ),
                ),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("last_processed_date", models.DateTimeField(blank=True, null=True)),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="notifications.template",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
