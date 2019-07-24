from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('webserver.polls.urls')),
    path('admin/', admin.site.urls),
]
