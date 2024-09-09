from django.shortcuts import render
from django.http import HttpResponse
from admin_section.models import *

# Create your views here.

def home(request):
    homeall = Home1.objects.exclude(isdelete=1)
    home = Home2.objects.exclude(isdelete=1)
    about = About.objects.exclude(isdelete=1)
    gallery = Gallery.objects.exclude(isdelete=1)
    member = Member.objects.exclude(isdelete=1)
    context = {
        'homeall': homeall,
        'home': home,
        'gallery': gallery,
        'member': member,
        'about' : about,
    }
    return render(request,'user_index.html',context)

def about(request):
    aboutall = About.objects.exclude(isdelete=1)
    return render(request,'user_about.html',{'aboutall':aboutall})

def gallery(request):
    pic = Gallery.objects.exclude(isdelete=1)
    return render(request,'user_gallery.html',{'pic':pic})

def contact(request):
    return render(request,'user_contact.html')

def service(request):
    services = Service.objects.exclude(isdelete=1)
    return render(request,'user_service.html',{'services':services})

