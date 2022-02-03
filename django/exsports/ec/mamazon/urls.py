from django.urls import path
from mamazon import views

app_name = 'mamazon'

urlpatterns = [
    path('', views.Home.as_view(), name='home')
]