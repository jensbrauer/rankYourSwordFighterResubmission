from . import views
from django.urls import path

urlpatterns = [
    path('', views.SwordfighterList.as_view(), name='home'),
    path('<slug:slug>/', views.SwordfighterDetail.as_view(), name='swordfighter_detail'),
    path('upvote/<slug:slug>', views.SwordfighterUpvote.as_view(), name="swordfighter_upvote"),
    path('contribute', views.Contribute.as_view(), name='contribute'),
    path('<name>', views.delete_swordfighter.as_view(), name='delete')
]

