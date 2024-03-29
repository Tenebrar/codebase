from django.urls import path

from webserver.polls.views import detail, index, results

app_name = 'polls'
urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
]