from django.urls import path
from . import views

app_name = 'vote'
urlpatterns = [
    path('', views.vote, name='vote'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('success', views.success, name='success'),
]
