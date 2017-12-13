from django.conf.urls import url
from . import views
from .forms import LoginForm
 
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile$', views.profile, name='profile'),
 
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),
 
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'auth/login.html', 'authentication_form': LoginForm},
        name='login'),
 
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'auth/index.html'},
        name='logout'),
]

