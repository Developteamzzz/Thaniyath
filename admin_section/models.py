from django.db import models

# # Create your models here.
class Home1(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class Home2(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class About(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class Service(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class Contact(models.Model):
    contact=models.CharField(max_length=100)
    email=models.CharField(max_length=800)
    address=models.CharField(max_length=100)
    map=models.CharField(max_length=800)
    facebook=models.CharField(max_length=800)
    whatsapp=models.CharField(max_length=800)
    twitter=models.CharField(max_length=800)
    instagram=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class Gallery(models.Model):
    image=models.CharField(max_length=100)
    description=models.CharField(max_length=800)
    title=models.CharField(max_length=100)
    year=models.CharField(max_length=800)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)

class Member(models.Model):
    image=models.CharField(max_length=100)
    name=models.CharField(max_length=800)
    role=models.CharField(max_length=100)
    added_on=models.DateTimeField(auto_now_add=True)
    added_by=models.IntegerField(default=0)
    isdelete=models.IntegerField(default=0)