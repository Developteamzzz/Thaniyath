from django.urls import path
from . import  views
urlpatterns = [
    path('',views.login, name='login'),
    path('index',views.index, name='index'),
    path('home_page',views.home_page, name='home_page'),
    path('list_home',views.list_home, name='list_home'),
    path('home_page2',views.home_page2, name='home_page'),
    path('home_upt/<int:id>/',views.home_upt, name='home_upt'),
    path('delete_home/<int:id>/',views.delete_home, name='delete_home'),
    path('about',views.about_page, name='about'),
    path('services',views.services_page, name='services'),
    path('list_gallery',views.list_gallery, name='list_gallery'),
    path('gallery_page',views.gallery_page, name='gallery_page'),
    path('gallery_upt/<int:id>/',views.gallery_upt, name='gallery_upt'),
    path('delete_gallery/<int:id>/',views.delete_gallery, name='delete_gallery'),
    path('contact',views.contact_page, name='contact'),
    path('member',views.member, name='member'),
    path('memberlist',views.memberlist, name='memberlist'),
    path('member_upt/<int:id>/',views.member_upt, name='member_upt'),
    path('delete_member/<int:id>/',views.delete_member, name='delete_member'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
]
