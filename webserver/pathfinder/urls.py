from django.urls import path

from webserver.pathfinder.views import character_sheet, character_sheet_test

app_name = 'pathfinder'
urlpatterns = [
    path('<int:character_id>/', character_sheet, name='character_sheet'),
    path('test/<int:character_id>/', character_sheet_test, name='character_sheet_test'),
]