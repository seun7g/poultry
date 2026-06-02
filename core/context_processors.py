from .models import SiteSettings, NavigationItem

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'nav_items': NavigationItem.objects.all(),
    }
