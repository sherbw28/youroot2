from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.utils import timezone
from cgitb import text
from tkinter import CASCADE
from turtle import title

class PrefeCode(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(47)])
    
    def __str__(self):
        return self.name
    
class TypeOfPlace(models.Model):
    TYPE_CHOICE = (
        ('eat','ご飯'),
        ('play','遊び'),
    )
    type = models.CharField(max_length=255, choices=TYPE_CHOICE)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    ido = models.FloatField(null=True)
    keido = models.FloatField(null=True)
    
    def __str__(self):
        return self.name


class Play(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    ido = models.FloatField(null=True)
    keido = models.FloatField(null=True)
    
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
