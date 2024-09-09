from django.shortcuts import render, redirect,  get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . models import *
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from django.utils import timezone
# Create your views here.

def login(request):
    email=request.POST.get('email')
    password=request.POST.get('password')
    # Hardcoded credentials check
    if email == 'admin@gmail.com' and password == 'admin':
       return render(request,'index.html')
    else:
      return render(request,'login.html')

def index(request):
    return render(request,'index.html')

def home_page(request):
    # Get the first non-deleted instance
    member = Home1.objects.exclude(isdelete=1).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if member:
            # Update existing member
            member.title = title
            member.description = description
            member.save()
        else:
            # Create new member if none exists
            Home1.objects.create(title=title, description=description)
        
        # Redirect to avoid re-posting on refresh
        return HttpResponseRedirect(reverse(home_page))
    
    return render(request, 'home_one.html', {'member': member})

def added_on(request,id):
    instance = Home1()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()

def home_page2(request):
    if request.method== 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        y=Home2(title=title,description=description)
        y.save()
    return render(request,'home_two.html')
   
def list_home(request):
    member = Home2.objects.exclude(isdelete=1)
    return render(request,'view_home.html',{'member':member})
         
def home_upt(request,id):
    member = Home2.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        member.title = title
        member.description = description
        member.save()
        return redirect('home_upt', id=id)
    return render(request,'home_update.html',{'member':member})
    
def delete_home(request,id):
   # Soft delete by marking is_deleted as 1
    home = get_object_or_404(Home2, id=id)
    home.isdelete = 1
    home.delete()
    home.save()
    return HttpResponseRedirect(reverse(list_home))

def added_on(request,id):
    instance = Home2()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()

def about_page(request):
     # Get the first non-deleted instance
    member = About.objects.exclude(isdelete=1).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if member:
            # Update existing member
            member.title = title
            member.description = description
            member.save()
        else:
            # Create new member if none exists
            About.objects.create(title=title, description=description)
        # Redirect to avoid re-posting on refresh
        return HttpResponseRedirect(reverse(about_page))

    return render(request, 'about.html', {'member': member})

def added_on(request,id):
    instance = About()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()


def services_page(request):
     # Get the first non-deleted instance
    member = Service.objects.exclude(isdelete=1).first()
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if member:
            # Update existing member
            member.title = title
            member.description = description
            member.save()
        else:
            # Create new member if none exists
            Service.objects.create(title=title, description=description)
        # Redirect to avoid re-posting on refresh
        return HttpResponseRedirect(reverse(services_page))

    return render(request,'services.html', {'member': member})


def added_on(request,id):
    instance = Service()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()


def gallery_page(request):
    if request.method== 'POST':
        image=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(image.name,image)
        description=request.POST.get('description')
        title=request.POST.get('title')
        year=request.POST.get('year')
        v=Gallery(title=title,description=description,year=year,image=image)
        v.save()
    return render(request,'gallery.html')

def list_gallery(request):
    member = Gallery.objects.exclude(isdelete=1)
    return render(request,'view_gallery.html',{'member':member})

def gallery_upt(request,id):
    member = get_object_or_404(Gallery, id=id)
    if request.method== 'POST':
        description=request.POST.get('description')
        title=request.POST.get('title')
        year=request.POST.get('year')
        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            member.image = filename
        member.description = description
        member.title = title
        member.year = year
        member.save()
        return redirect('gallery_upt', id=id)
    return render(request,'gallery_update.html',{'member':member})

def delete_gallery(request,id):
   # Soft delete by marking is_deleted as 1
    gallery= get_object_or_404(Gallery, id=id)
    gallery.isdelete = 1
    gallery.delete()
    gallery.save()
    return HttpResponseRedirect(reverse(list_gallery))

def added_on(request,id):
    instance = Gallery()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()

def contact_page(request):
    member = Contact.objects.exclude(isdelete=1).first()
    if request.method== 'POST':
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        address=request.POST.get('address')
        map=request.POST.get('map')
        facebook=request.POST.get('facebook')
        whatsapp=request.POST.get('whatsapp')
        twitter=request.POST.get('twitter')
        instagram=request.POST.get('instagram')
        if member:
            member.contact=contact
            member.email=email
            member.address=address
            member.map=map
            member.facebook=facebook
            member.whatsapp=whatsapp
            member.twitter=twitter
            member.instagram=instagram
            member.save()
        else:
            Contact.objects.create(contact=contact,email=email,address=address,map=map,facebook=facebook,whatsapp=whatsapp,twitter=twitter,instagram=instagram)
        return HttpResponseRedirect(reverse(contact_page))
    return render(request,'contact.html',{'member':member})

def added_on(request,id):
    instance = Contact()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()


def member(request):
    if request.method== 'POST':
        image=request.FILES['image']
        fs=FileSystemStorage()
        f=fs.save(image.name,image)
        name=request.POST.get('name')
        role=request.POST.get('role')
        r=Member(name=name,role=role,image=image)
        r.save()
    return render(request,'member.html')

def memberlist(request):
    member = Member.objects.exclude(isdelete=1)
    return render(request,'view_member.html',{'member':member})

def member_upt(request,id):
    member = get_object_or_404(Member, id=id)
    if request.method== 'POST':
        name=request.POST.get('name')
        role=request.POST.get('role')
        if 'image' in request.FILES:
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name,image)
            member.image = filename
        member.name = name
        member.role = role
        member.save()
        return redirect('member_upt', id=id)
    return render(request,'member_update.html',{'member':member})

def delete_member(request,id):
   # Soft delete by marking is_deleted as 1
    member= get_object_or_404(Member, id=id)
    member.isdelete = 1
    member.delete()
    member.save()
    return HttpResponseRedirect(reverse('memberlist'))

def added_on(request,id):
    instance = Member()
    instance.added_on = timezone.now()  # Set added_on field to current date and time
    instance.save()

    
def logout(request):
    return redirect('login')  
   