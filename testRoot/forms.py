from dataclasses import fields
from django import forms
from .models import Play, Eat

class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ('name','address','pref','ido','keido')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address'}),
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id':'ido'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度','id':'keido'}),
        }
        
class EatForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ('name','address','pref','ido','keido')
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address'}),
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido'}),
        }