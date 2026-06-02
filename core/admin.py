from django.contrib import admin
from .models import ContactInfo, AboutUs, SiteSettings, NavigationItem

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)

@admin.register(NavigationItem)
class NavigationItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')
    list_editable = ('order',)
