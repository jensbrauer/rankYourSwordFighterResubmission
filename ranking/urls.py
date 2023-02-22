from . import views
from django.urls import path

urlpatterns = [
    path('', views.swordfighterList.as_view(), name='home')
]