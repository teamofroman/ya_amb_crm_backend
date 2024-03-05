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
        ("merches", "0003_alter_ambassadorrequest_assignment_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ambassadorrequest",
            name="ambassador",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassador_requests",
                to="ambassador.ambassador",
            ),
        ),
        migrations.AlterField(
            model_name="ambassadorrequest",
            name="merch_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="ambassador_requests",
                to="merches.merchrequest",
            ),
        ),
        migrations.AlterField(
            model_name="deliveryhistory",
            name="delivery_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="delivery_history",
                to="merches.deliverystatus",
                verbose_name="Статус доставки",
            ),
        ),
        migrations.AlterField(
            model_name="deliveryhistory",
            name="merch_request",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="delivery_history",
                to="merches.merchrequest",
                verbose_name="Запрос на мерч",
            ),
        ),
        migrations.AlterField(
            model_name="merchrequest",
            name="delivery_address",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to="merches.deliveryaddress",
                verbose_name="Адрес доставки",
            ),
        ),
        migrations.AlterField(
            model_name="merchrequest",
            name="manager",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Менеджер",
            ),
        ),
        migrations.AlterField(
            model_name="merchrequest",
            name="merch",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to="merches.merch",
                verbose_name="Мерч",
            ),
        ),
        migrations.AlterField(
            model_name="merchrequest",
            name="request_status",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="merch_requests",
                to="merches.deliverystatus",
                verbose_name="Статус выполнения",
            ),
        ),
    ]
