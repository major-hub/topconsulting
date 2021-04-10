from django.contrib import admin

from landing.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_answered')
    list_filter = ('sent_at', 'is_answered')
    search_fields = ('name', )
    list_editable = ('is_answered', )
    list_per_page = 10
