# Generated by Django 4.2.7 on 2024-02-29 05:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm_messages", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="botmessages",
            name="manager_id",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AddField(
            model_name="botmessages",
            name="message_id",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="crm_messages.message",
                verbose_name="Сообщение",
            ),
        ),
    ]
