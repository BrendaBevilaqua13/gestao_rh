from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_core,name='home_core'),
]
