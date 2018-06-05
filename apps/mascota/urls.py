from django.urls import path, include
from apps.mascota.views import index_mascota
app_name = 'apps'
urlpatterns = [
     path('', index_mascota),
]