from django.shortcuts import render, redirect
from .models import Play, Eat
from .forms import PlayForm, EatForm
import random

def index(request):
    return render(request, 'testRoot/index.html')

def list_play(request):
    lists = Play.objects.filter(pk=1)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_play.html', content)

def list_eat(request):
    x = random.randint(1,6)
    lists = Eat.objects.filter(pk=x)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_eat.html', content)

def test(request):
    return render(request, 'testRoot/test.html')

def list_all(request):
    lists_play = Play.objects.all()
    lists_eat = Eat.objects.all()
    x = random.randint(1,len(lists_play))
    y = random.randint(1,len(lists_eat))
    z = random.randint(1,len(lists_play))
    while x == z:
        z = random.randint(1,len(lists_play))
    
    list_1 = Play.objects.filter(pk=x)
    list_2 = Eat.objects.filter(pk=y)
    list_3 = Play.objects.filter(pk=z)
    lists = [list_1, list_2, list_3]
    
    content = {
        'list_1': list_1,
        'list_2': list_2,
        'list_3': list_3,
        'lists': lists,
    }
    return render(request, 'testRoot/list_all.html', content)

def test_direction(request):
    return render(request, 'testRoot/test_direction.html')

def rootDisplay(request):
    lists_play = Play.objects.all()
    lists_eat = Eat.objects.all()
    x = random.randint(1,len(lists_play))
    y = random.randint(1,len(lists_eat))
    z = random.randint(1,len(lists_play))
    while x == z:
        z = random.randint(1,len(lists_play))
        
    list_1 = Play.objects.filter(pk=x)
    list_2 = Eat.objects.filter(pk=y)
    list_3 = Play.objects.filter(pk=z)
    lists = [list_1, list_2, list_3]
    
    
    for i, list in enumerate(lists):
        for date in list:
            if i == 0:
                address1 = date.address
            elif i == 1:
                address2 = date.address
            else:
                address3 = date.address
    
    
    
    content = {
        'address1': address1,
        'address2': address2,
        'address3': address3,
        'lists': lists
    }
    
    return render(request, 'testRoot/rootDisplay.html', content)

def test1(request):
    lists_play = Play.objects.all()
    lists_eat = Eat.objects.all()
    x = random.randint(1,len(lists_play))
    y = random.randint(1,len(lists_eat))
    z = random.randint(1,len(lists_play))
    while x == z:
        z = random.randint(1,len(lists_play))
        
    list_1 = Play.objects.filter(pk=x)
    list_2 = Eat.objects.filter(pk=y)
    list_3 = Play.objects.filter(pk=z)
    lists = [list_1, list_2, list_3]
    
    
    for i, list in enumerate(lists):
        for date in list:
            if i == 0:
                address1 = date.address
                ido1 = date.ido
                keido1 = date.keido
            elif i == 1:
                address2 = date.address
                ido2 = date.ido
                keido2 = date.keido
            else:
                address3 = date.address
                ido3 = date.ido
                keido3 = date.keido
    
    
    
    content = {
        'address1': address1,
        'address2': address2,
        'address3': address3,
        'ido1':ido1,
        'keido1':keido1,
        'ido2':ido2,
        'keido2':keido2,
        'ido3':ido3,
        'keido3':keido3,
        'lists': lists
    }
    return render(request, 'testRoot/test1.html', content)

def test2(request):
    if request.method == "POST":
        form = PlayForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = PlayForm()
    return render(request, 'testRoot/test2.html', {'form': form})

def test3(request):
    return render(request, 'testRoot/test3.html')

def test4(request):
    return render(request, 'testRoot/test4.html')

def test5(request):
    return render(request, 'testRoot/test5.html')