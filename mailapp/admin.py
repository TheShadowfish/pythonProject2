from django.contrib import admin

from mailapp.models import Client, Mailing, MailingLog


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'message', 'created_at',)
    list_filter = ('title',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'comment', 'is_active', 'mailing')
    list_filter = ('email',)


@admin.register(MailingLog)
class MailingLogAdmin(admin.ModelAdmin):
    list_display = ('log_text', 'mailing', 'created_at',)
    list_filter = ('mailing',)
