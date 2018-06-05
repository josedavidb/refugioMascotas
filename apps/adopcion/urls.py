from django.urls import path, include
from apps.adopcion.views import index_adopcion
app_name = 'apps'
urlpatterns = [
     path('', index_adopcion),
]