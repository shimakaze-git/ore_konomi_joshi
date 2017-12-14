from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
 
app_name = 'user'
 

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^regist_save/$', views.regist_save, name='regist_save'),
    
    
    url(
        r'^login/$',
        auth_views.login,
        {'template_name': 'user/login.html', 'authentication_form': LoginForm},
        # {'template_name': 'user/login.html'},
        name='login'
    ),
    url(
        r'^logout/$',
        auth_views.logout,
        {'template_name': 'user/index.html'},
        name='logout'
    ),
]