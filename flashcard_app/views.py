from django.shortcuts import render, redirect
from .models import FlashcardSet, Flashcard
from .forms import FlashcardSetForm, FlashcardForm

def create_flashcard_set(request):
    if request.method == 'POST':
        form = FlashcardSetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_sets')
    else:
        form = FlashcardSetForm()
    return render(request, 'flashcard_app/create_flashcard_set.html', {'form': form})

def create_flashcard(request, set_id):
    flashcard_set = FlashcardSet.objects.get(id=set_id)
    if request.method == 'POST':
        form = FlashcardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flashcard_set_detail', set_id=set_id)
    else:
        form = FlashcardForm(initial={'flashcard_set': flashcard_set})
    return render(request, 'flashcard_app/create_flashcard.html', {'form': form, 'flashcard_set': flashcard_set})

def flashcard_sets(request):
    sets = FlashcardSet.objects.all()
    return render(request, 'flashcard_app/flashcard_sets.html', {'sets': sets})

def flashcard_set_detail(request, set_id):
    flashcard_set = FlashcardSet.objects.get(id=set_id)
    flashcards = flashcard_set.flashcards.all()
    return render(request, 'flashcard_app/flashcard_set_detail.html', {'flashcard_set': flashcard_set, 'flashcards': flashcards})

def study_flashcards(request, set_id):
    flashcard_set = FlashcardSet.objects.get(id=set_id)
    flashcards = flashcard_set.flashcards.filter(hidden=False)
    return render(request, 'flashcard_app/study_flashcards.html', {'flashcards': flashcards})
