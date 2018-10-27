from django.urls import path

from . import views

app_name = 'charsheet'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:character_id>/', views.sheet, name='sheet'),
    path('<int:character_id>/detail', views.detail, name='detail'),
    path('<int:character_id>/add_roll', views.add_roll, name='add_roll'),
]
