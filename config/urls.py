from unicodedata import name
from django.contrib import admin
from django.urls import path, include
# from testRoot.views import index, list_play, list_eat, test, list_all, test_direction, rootDisplay, test1, test2, test3, test4, test5, user, save, detail, like, topPage, topPage1
from testRoot.views import index, test_direction, test1, test2, user, detail, like, topPage, topPage1, topIndex, savecomment, saveevaluation, test3
# from testRoot.views import list_play, list_eat, test, list_all, rootDisplay, test3, test4, test5, save
from django.views.generic import RedirectView
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='youroot/topPage')),
    path('youroot/', index, name='index'),
    path('testRoot/test_direction', test_direction, name='test_direction'),
    path('youroot/result', test1, name='test1'),
    path('youroot/register', test2, name='test2'),
    path('user/<int:id>', user, name='user'),
    path('youroot/<int:id>/detail', detail, name='detail'),
    path('youroot/<int:id>/like', like, name='like'),
    path('youroot/topPage', topPage, name='topPage'),
    path('topPage/', topPage1, name='topPage1'),
    path('accounts/logout/topIndex/', topIndex, name='topIndex'),
    path('savecomment', savecomment, name='savecomment'),
    path('saveevaluation', saveevaluation, name="saveevaluation"),
    path('youroot/test3', test3, name='test3')
    # path('testRoot/list_play', list_play, name='list_play'),
    # path('testRoot/list_eat', list_eat, name='list_eat'),
    # path('testRoot/list_all', list_all, name='list_all'),
    # path('testRoot/test', test, name='test'),
    # path('testRoot/test3', test3, name='test3'),
    # path('testRoot/test4', test4, name='test4'),
    # path('testRoot/test5', test5, name='test5'),
    # path('testRoot/save', save, name='save'),
    # path('testRoot/rootDisplay', rootDisplay, name='rootDisplay'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)