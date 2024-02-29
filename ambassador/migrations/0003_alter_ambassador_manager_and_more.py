# Generated by Django 4.2.7 on 2024-02-29 19:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("ambassador", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ambassador",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                max_length=50,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AlterField(
            model_name="ambassador",
            name="middle_name",
            field=models.CharField(
                blank=True, max_length=50, null=True, verbose_name="Отчество"
            ),
        ),
    ]
