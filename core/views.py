from django.shortcuts import render
from .models import AboutUs, ContactInfo

def index(request):
    about_us = AboutUs.objects.all()
    contact_info = ContactInfo.objects.all()
    context = {
        'about_us': about_us,
        'contact_info': contact_info,
    }
    return render(request, 'index.html', context)
