from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class PrefeCode(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(47)])
    
    def __str__(self):
        return self.name


class Play(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
    
class Eat(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    pref = models.ForeignKey(PrefeCode, on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.name
