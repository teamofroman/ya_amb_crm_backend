# Generated by Django 4.2.7 on 2024-03-05 21:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        (
            "ambassador",
            "0004_alter_ambassador_manager_alter_ambassador_status_and_more",
        ),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("crm_messages", "0003_alter_message_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="botmessages",
            name="ambassador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bot_messages",
                to="ambassador.ambassador",
                verbose_name="Амбасcадор",
            ),
        ),
        migrations.AlterField(
            model_name="botmessages",
            name="manager",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bot_messages",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AlterField(
            model_name="botmessages",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="bot_messages",
                to="crm_messages.message",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AlterField(
            model_name="message",
            name="message_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="messages",
                to="crm_messages.messagetype",
            ),
        ),
        migrations.AlterField(
            model_name="messagepool",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="messages_pool",
                to="crm_messages.message",
                verbose_name="Сообщение",
            ),
        ),
        migrations.AlterField(
            model_name="messagepool",
            name="message_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="messages_pool",
                to="crm_messages.messagestatus",
            ),
        ),
    ]
