from django.urls import path
from . import views

urlpatterns = [
    path('flashcard_sets/', views.flashcard_sets, name='flashcard_sets'),
    path('flashcard_set/<int:set_id>/', views.flashcard_set_detail, name='flashcard_set_detail'),
    path('create_flashcard_set/', views.create_flashcard_set, name='create_flashcard_set'),
    path('create_flashcard/<int:set_id>/', views.create_flashcard, name='create_flashcard'),
    path('study_flashcards/<int:set_id>/', views.study_flashcards, name='study_flashcards'),
]
