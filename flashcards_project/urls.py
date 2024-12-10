from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('flashcard_app.urls')), 
    path('', include('flashcard_app.urls')),    
]
