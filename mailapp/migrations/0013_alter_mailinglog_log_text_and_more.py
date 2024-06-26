# Generated by Django 5.0.6 on 2024-06-13 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailapp", "0012_alter_mailinglog_log_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailinglog",
            name="log_text",
            field=models.TextField(
                default=datetime.datetime(
                    2024, 6, 13, 11, 8, 49, 387221, tzinfo=datetime.timezone.utc
                ),
                help_text="введите текст лога",
                verbose_name="текст лога",
            ),
        ),
        migrations.AlterField(
            model_name="mailingsettings",
            name="periodicity",
            field=models.PositiveSmallIntegerField(
                default="1",
                help_text="введите периодичность",
                verbose_name="периодичность (через сколько дней)",
            ),
        ),
    ]
