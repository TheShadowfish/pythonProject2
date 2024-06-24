# Generated by Django 4.2.2 on 2024-06-24 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailapp", "0032_alter_mailinglog_log_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailinglog",
            name="log_text",
            field=models.TextField(
                default=datetime.datetime(
                    2024, 6, 24, 17, 44, 23, 380398, tzinfo=datetime.timezone.utc
                ),
                help_text="введите текст лога",
                verbose_name="текст лога",
            ),
        ),
    ]
