# Generated by Django 4.2.7 on 2024-02-29 19:40

import uuid

import django.db.models.deletion
from django.db import migrations, models

import reports.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0001_initial"),
    ]

    operations = [
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
                        max_length=100,
                        unique=True,
                        verbose_name="Площадка размещения контента",
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Площадка размещения отчета",
                "verbose_name_plural": "Площадки размещения отчетов",
            },
        ),
        migrations.CreateModel(
            name="ReportStatus",
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
                ("status_name", models.CharField(max_length=100, unique=True)),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статус отчета",
                "verbose_name_plural": "Статусы отчетов",
            },
        ),
        migrations.CreateModel(
            name="ReportType",
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
                    "type_name",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="Вид задания"
                    ),
                ),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность"
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип задания",
                "verbose_name_plural": "Типы заданий",
            },
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
                    models.DateField(
                        auto_now_add=True, verbose_name="Дата отчета"
                    ),
                ),
                (
                    "content_link",
                    models.URLField(
                        help_text="Добавьте ссылку на контент",
                        verbose_name="Ссылка на контент",
                    ),
                ),
                (
                    "screen",
                    models.FileField(
                        default=None,
                        null=True,
                        upload_to="reports/",
                        verbose_name="Скриншот",
                    ),
                ),
                (
                    "sign_junior",
                    models.BooleanField(
                        default=False, verbose_name="Начинающий амбассадор?"
                    ),
                ),
                (
                    "grade",
                    models.PositiveSmallIntegerField(
                        validators=[reports.validators.validate_one_to_ten]
                    ),
                ),
                (
                    "ambassador",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="ambassador.ambassador",
                    ),
                ),
                (
                    "placement",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="reports.placement",
                    ),
                ),
                (
                    "report_status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="reports.reportstatus",
                    ),
                ),
                (
                    "report_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="reports.reporttype",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отчет о задании",
                "verbose_name_plural": "Отчеты о заданиях",
            },
        ),
    ]
