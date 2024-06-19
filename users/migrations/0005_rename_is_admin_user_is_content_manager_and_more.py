# Generated by Django 4.2.2 on 2024-06-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0004_alter_user_managers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="is_admin",
            new_name="is_content_manager",
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                verbose_name="active",
            ),
        ),
    ]