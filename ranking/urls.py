from . import views
from django.urls import path

urlpatterns = [
    path('', views.LandingPage.as_view(), name='home'),
    path('ranking', views.SwordfighterList.as_view(), name='ranking'),
    path('page/<slug:slug>/', views.SwordfighterDetail.as_view(), name='swordfighter_detail'),
    path('upvote/<slug:slug>', views.SwordfighterUpvote.as_view(), name="swordfighter_upvote"),
    path('contribute', views.Contribute.as_view(), name='contribute'),
    path('delete/<slug>/', views.Delete_swordfighter.as_view(), name='delete'),
    path('edit/<slug>/', views.edit_swordfighter.as_view(), name='edit'),
    path('flag/<id>', views.FlagComment.as_view(), name='flag_comment'),
    path('delete_comment/<id>', views.DeleteComment.as_view(), name='delete_comment'),
]

