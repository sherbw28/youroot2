from django.shortcuts import render
from .models import Play, Eat
import random

def index(request):
    return render(request, 'testRoot/index.html')

def list_play(request):
    # lists = Play.objects.all()
    lists = Play.objects.filter(pk=1)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_play.html', content)

def list_eat(request):
    # lists = Eat.objects.all()
    x = random.randint(1,5)
    lists = Eat.objects.filter(pk=x)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_eat.html', content)

def test(request):
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
    lists = [list_1,list_2,list_3]
        
    content = {
        'x':x,
        'y':y,
        'z':z,
        'list_1': list_1,
        'list_2': list_2,
        'list_3': list_3,
        'lists':lists,
    }
    return render(request, 'testRoot/test.html', content)

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
    address1 = ""
    address2 = ""
    address3 = ""
    
    
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