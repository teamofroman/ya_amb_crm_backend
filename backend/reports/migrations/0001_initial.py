# Generated by Django 4.2.7 on 2024-02-25 15:16

import uuid

import django.db.models.deletion
from django.db import migrations, models

import backend.reports.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ambassador",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Placement",
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
                (
                    "site",
                    models.CharField(
                        max_length=100, verbose_name="Площадка размещения контента"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RunStatus",
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
                ("run_status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="TypeReport",
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
                (
                    "type_report",
                    models.CharField(max_length=100, verbose_name="Вид задания"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Report",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID Отчета",
                    ),
                ),
                (
                    "report_date",
                    models.DateField(auto_now=True, verbose_name="Дата отчета"),
                ),
                (
                    "content_link",
                    models.URLField(
                        help_text="Добавьте ссылку на контент",
                        unique=True,
                        verbose_name="Ссылка на контент",
                    ),
                ),
                (
                    "screen",
                    models.FileField(
                        default=None, null=True, upload_to="media/reports/screens/"
                    ),
                ),
                ("sign_junior", models.BooleanField()),
                (
                    "grade",
                    models.PositiveSmallIntegerField(
                        validators=[backend.reports.validators.validate_one_to_ten]
                    ),
                ),
                (
                    "id_ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.ambassador",
                    ),
                ),
                (
                    "id_run_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.runstatus",
                    ),
                ),
                (
                    "placement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reports.placement",
                    ),
                ),
            ],
        ),
    ]
