from random import choice, choices
from urllib import request
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.forms import ChoiceField
from django.utils import timezone
from cgitb import text
from tkinter import CASCADE
from turtle import title
from django.contrib.auth import get_user_model

class PrefeCode(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(47)])
    
    def __str__(self):
        return self.name
    
class City(models.Model):
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT)
    city_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.city_name
    
class Atmosphere(models.Model):
    type = models.CharField(max_length=255)
    
    def __str__(self):
        return self.type
    
class TypeOfPlace(models.Model):
    TYPE_CHOICE = (
        ('eat','ご飯'),
        ('play','遊び'),
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICE)
    name = models.CharField(max_length=255)
    atmosphere = models.ForeignKey(Atmosphere, on_delete=models.PROTECT, null=True)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    city = models.CharField(max_length=255, null=True)
    ido = models.FloatField(null=True)
    keido = models.FloatField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)
    good = models.IntegerField(null=True, default=0)
    comment = models.CharField(max_length=500, null=True)
    
    def __str__(self):
        return self.name
    
class CommentDetail(models.Model):
    comment = models.CharField(max_length=255)
    comment_place = models.ForeignKey(TypeOfPlace, on_delete=models.PROTECT)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.comment
    
class SaveRoot(models.Model):
    rootName = models.CharField(max_length=255)
    name1 = models.CharField(max_length=255)
    address1 = models.CharField(max_length=255)
    ido1 = models.FloatField(null=True)
    keido1 = models.FloatField(null=True)
    name2 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    ido2 = models.FloatField(null=True)
    keido2 = models.FloatField(null=True)
    name3 = models.CharField(max_length=255)
    address3 = models.CharField(max_length=255)
    ido3 = models.FloatField(null=True)
    keido3 = models.FloatField(null=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.rootName


class Play(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    ido = models.FloatField(null=True)
    keido = models.FloatField(null=True)
    image = models.ImageField(upload_to='images/', null=True)
    
    def __str__(self):
        return self.name
    
    
class Eat(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    ido = models.FloatField(null=True)
    keido = models.FloatField(null=True)
    
    def __str__(self):
        return self.name
    
class KeepRoot(models.Model):
    name = models.CharField(max_length=255)
    first = models.ForeignKey(TypeOfPlace, on_delete=models.CASCADE, null=True,related_name='first')
    second = models.ForeignKey(TypeOfPlace, on_delete=models.CASCADE, null=True,related_name='second')
    third = models.ForeignKey(TypeOfPlace, on_delete=models.CASCADE, null=True,related_name='third')
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name