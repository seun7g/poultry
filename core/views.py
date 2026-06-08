from django.shortcuts import render
from .models import AboutUs, ContactInfo, Project

def index(request):
    about_us = AboutUs.objects.all()
    contact_info = ContactInfo.objects.all()
    context = {
        'about_us': about_us,
        'contact_info': contact_info,
    }
    return render(request, 'index.html', context)

def about(request):
    about_us = AboutUs.objects.all()
    return render(request, 'about.html', {'about_us': about_us})

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects_list})
