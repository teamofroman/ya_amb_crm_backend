# Generated by Django 4.2.7 on 2024-02-29 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("achievements", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ambassadorachieve",
            name="assignment_date",
            field=models.DateField(verbose_name="Дата получения ачивки"),
        ),
    ]
