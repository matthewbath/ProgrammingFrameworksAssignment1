from django.db import models

class FlashcardSet(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Flashcard(models.Model):
    flashcard_set = models.ForeignKey(FlashcardSet, on_delete=models.CASCADE, related_name='flashcards')
    question = models.TextField()
    answer = models.TextField()
    hidden = models.BooleanField(default=False)  # Add a hidden field to mark cards as hidden

    def __str__(self):
        return f"Question: {self.question}"

    def is_hidden(self):
        return self.hidden
