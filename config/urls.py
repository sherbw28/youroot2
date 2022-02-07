from django.contrib import admin
from django.urls import path
from testRoot.views import index, list_play, list_eat, test, list_all, test_direction, rootDisplay
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', RedirectView.as_view(url='testRoot/')),
    path('testRoot/', index, name='index'),
    path('testRoot/list_play', list_play, name='list_play'),
    path('testRoot/list_eat', list_eat, name='list_eat'),
    path('testRoot/test', test, name='test'),
    path('testRoot/list_all', list_all, name='list_all'),
    path('testRoot/test_direction', test_direction, name='test_direction'),
    path('testRoot/rootDisplay', rootDisplay, name='rootDisplay'),
]
