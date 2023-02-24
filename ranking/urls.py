from . import views
from django.urls import path

urlpatterns = [
    path('', views.swordfighterList.as_view(), name='home'),
    path('<slug:slug>/', views.swordfighterDetail.as_view(), name='swordfighter_detail'),
]