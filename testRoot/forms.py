from dataclasses import fields
from django import forms
from .models import Play, Eat, TypeOfPlace, City, PrefeCode

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
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido2'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido2'}),
        }
        
class TypeOfPlaceForm(forms.ModelForm):
    class Meta:
        model = TypeOfPlace
        fields = '__all__'
        labels={
           'type':'種類',
           'atmosphere':"雰囲気",
           'name':'名前',
           'address':'住所',
           'pref':'所在地',
           'city':'市町村',
           'image':"画像"
           }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName1'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address1', 'type':'hidden'}),
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido1', 'type':'hidden'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido1', 'type':'hidden'}),
        }
        