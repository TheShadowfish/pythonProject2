# Generated by Django 5.0.6 on 2024-06-12 09:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailapp', '0005_message_alter_mailinglog_log_text_mailinglog_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglog',
            name='message',
        ),
        migrations.AlterField(
            model_name='mailinglog',
            name='log_text',
            field=models.TextField(default=datetime.datetime(2024, 6, 12, 9, 21, 7, 890987, tzinfo=datetime.timezone.utc), help_text='введите текст лога', verbose_name='текст лога'),
        ),
    ]
