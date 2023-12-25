


from django.contrib import admin
from django.urls import path,include
from .api import LocationAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('location/',LocationAPI.as_view()),
    
]
