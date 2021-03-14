from django.urls import path
from . import views


urlpatterns = [
    path('', views.menu, name='menu'),
    path('contattaci', views.contattaci, name='contattaci'),
]