from dataclasses import fields
from operator import attrgetter
from tkinter import Widget
from django import forms
from .models import Play, Eat, TypeOfPlace, City, PrefeCode, SaveRoot, KeepRoot, CommentDetail, Evaluation, GoodCheck, TokyoCity

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
           'image':"画像",
           'comment': 'コメント',
           }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName1'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address1', 'type':'hidden'}),
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido1', 'type':'hidden'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido1', 'type':'hidden'}),
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'good': forms.TextInput(attrs={'type':'hidden'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '一言コメント!'}),
        }
        
class TokyoCityForm(forms.ModelForm):
    class Meta:
        model = TokyoCity
        fields = '__all__'
        labels={
           'type':'種類',
           'atmosphere':"雰囲気",
           'name':'名前',
           'address':'住所',
           'city':'市町村',
           'image':"画像",
           'comment': 'コメント',
           }
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName1'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address1', 'type':'hidden'}),
            'ido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido1', 'type':'hidden'}),
            'keido': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido1', 'type':'hidden'}),
            'author': forms.TextInput(attrs={'type': 'hidden'}),
            'good': forms.TextInput(attrs={'type':'hidden'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '一言コメント!'}),
        }

class SaveRootForm(forms.ModelForm):
    class Meta:
        model = SaveRoot
        fields = '__all__'
        widgets = {
            'rootName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'name1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName11', 'type': 'hidden'}),
            'address1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address11', 'type': 'hidden'}),
            'ido1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido11', 'type': 'hidden'}),
            'keido1': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido11','type': 'hidden'}),
            'name2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName22', 'type': 'hidden'}),
            'address2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address22', 'type': 'hidden'}),
            'ido2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido22', 'type': 'hidden'}),
            'keido2': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido22', 'type': 'hidden'}),
            'name3': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'name', 'id': 'subsName33', 'type': 'hidden'}),
            'address3': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'address', 'id':'address33', 'type': 'hidden'}),
            'ido3': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'緯度', 'id': 'ido33', 'type': 'hidden'}),
            'keido3': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'経度', 'id': 'keido33', 'type': 'hidden'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userName', 'id': 'author1', 'type': 'hidden'}),
        }
        
class KeepRootForm(forms.ModelForm):
    class Meta:
        model = KeepRoot
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ルート名前'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userName', 'id': 'author1', 'type': 'hidden'}),
            'first': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first', 'id': 'first', 'type': 'hidden'}),
            'second': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'second', 'id': 'second', 'type': 'hidden'}),
            'third': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'third', 'id': 'third', 'type': 'hidden'}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentDetail
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userName', 'id': 'author1', 'type': 'hidden'}),
            'comment_place': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'コメント'}),
        }
        
class EvaluationForm(forms.ModelForm):
    class Meta:
        model = Evaluation
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userName', 'id': 'author1'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class GoodCheckForm(forms.ModelForm):
    class Meta:
        model = GoodCheck
        fields = '__all__'
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'userName'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
        }