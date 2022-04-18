from django.urls import path
from . import views
from .views import profile

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', profile, name='users-profile'),
]
