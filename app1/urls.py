from django.urls import path
from .views import *


# It helps Django identify URLs of a specific app when multiple apps exist in a project.

# Many Django projects contain multiple apps, and different apps may have same URL names like index, login, detail, etc.

# app_name prevents URL name conflicts.

# If another app also has index, Django will get confused and throw an error

# <a href="{% url 'app:index' %}">Home</a>

# movies_app:index
# accounts_app:index

app_name='app1'

urlpatterns=[
    path('index/',index,name='index'),
    path('',home,name='home'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('signup/',signup,name='signup'),
    path('search/',search,name='search'),
    path('my_list/',my_list,name='my_list'),
    path('movie/<str:pk>',movie,name='movie'),
    path('genre/<str:pk>',genre,name='genre'),
    path('add_to_list/',add_to_list,name='add_to_list')


]