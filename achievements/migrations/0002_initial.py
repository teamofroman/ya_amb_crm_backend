# Generated by Django 4.2.7 on 2024-02-29 05:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("ambassador", "0001_initial"),
        ("achievements", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ambassadorachieve",
            name="ambassador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="ambassador.ambassador",
            ),
        ),
    ]
