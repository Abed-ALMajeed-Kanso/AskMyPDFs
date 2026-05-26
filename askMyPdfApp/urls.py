from django.urls import path
from .views import home, manage_files

urlpatterns = [
    path('', home, name='home'),
    path('manage-files/', manage_files, name='manage_files'),
]