from .models import SiteSettings, NavigationItem, UserProfile

def site_settings(request):
    return {
        'site_settings': SiteSettings.objects.first(),
        'nav_items': NavigationItem.objects.all(),
        'user_profile': UserProfile.objects.first(),
    }
