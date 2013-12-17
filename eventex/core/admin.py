from django.contrib import admin
from eventex.core.models import Speaker, Contact


class ContactInlineAdmin(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    fields = ['name', 'slug', 'url', 'description']
    inlines = [ContactInlineAdmin,]


admin.site.register(Speaker, SpeakerAdmin)