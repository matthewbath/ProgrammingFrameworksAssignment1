from django.test import TestCase
from django.urls import reverse
from flashcard_app.models import FlashcardSet, Flashcard
from django.contrib.auth.models import User

class FlashcardSetTests(TestCase):

    def setUp(self):
        # Create a set
        self.flashcard_set = FlashcardSet.objects.create(name='Math Set', created_by=self.user)
        # Create Flashcards
        Flashcard.objects.create(question='What is 2 + 2?', answer='4', flashcard_set=self.flashcard_set)
        Flashcard.objects.create(question='What is 3 + 3?', answer='6', flashcard_set=self.flashcard_set)

    def test_flashcard_set_creation(self):
        """Test if a flashcard set is created successfully"""
        self.assertEqual(self.flashcard_set.name, 'Math Set')
        self.assertEqual(self.flashcard_set.flashcard_set.count(), 2)  # Check if 2 flashcards were created

    def test_flashcard_list_view(self):
        """Test if the flashcard list view returns the correct status code"""
        response = self.client.get(reverse('flashcard_set_list'))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Math Set')

    def test_flashcard_detail_view(self):
        """Test if the flashcard detail view shows the correct content"""
        flashcard = self.flashcard_set.flashcard_set.first()  # Get the first flashcard
        response = self.client.get(reverse('flashcard_detail', kwargs={'pk': flashcard.pk})) 
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is 2 + 2?')
        self.assertContains(response, '4')

    def test_create_flashcard(self):
        """Test if a flashcard can be created via a POST request"""
        data = {
            'question': 'What is 5 + 5?',
            'answer': '10',
            'flashcard_set': self.flashcard_set.id,
        }
        response = self.client.post(reverse('flashcard_create'), data) 
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Flashcard.objects.count(), 3)  

    def test_user_login_required(self):
        """Test if a user is required to be logged in to access certain views"""
        response = self.client.get(reverse('flashcard_create'))  
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, '/login/?next=/flashcards/create/')  

class FlashcardTests(TestCase):

    def setUp(self):
        # Create a set
        self.flashcard_set = FlashcardSet.objects.create(name='Math Set', created_by=self.user)
        # Create Flashcards
        self.flashcard1 = Flashcard.objects.create(question='What is 2 + 2?', answer='4', flashcard_set=self.flashcard_set)
        self.flashcard2 = Flashcard.objects.create(question='What is 3 + 3?', answer='6', flashcard_set=self.flashcard_set)

    def test_flashcard_creation(self):
        """Test that a flashcard is created correctly"""
        self.assertEqual(self.flashcard1.question, 'What is 2 + 2?')
        self.assertEqual(self.flashcard1.answer, '4')
        self.assertEqual(self.flashcard1.flashcard_set, self.flashcard_set)

    def test_flashcard_list_view(self):
        """Test the view for listing flashcards"""
        response = self.client.get(reverse('flashcard_list', kwargs={'flashcard_set_id': self.flashcard_set.id}))  
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'What is 2 + 2?')
        self.assertContains(response, 'What is 3 + 3?')

    def test_flashcard_toggle_answer(self):
        """Test if the answer toggle functionality works"""
        response = self.client.get(reverse('flashcard_detail', kwargs={'pk': self.flashcard1.pk})) 
        self.assertContains(response, 'What is 2 + 2?')
        self.assertNotContains(response, '4')  
        response = self.client.post(reverse('flashcard_toggle_answer', kwargs={'pk': self.flashcard1.pk}))  
        self.assertEqual(response.status_code, 302) 
        response = self.client.get(reverse('flashcard_detail', kwargs={'pk': self.flashcard1.pk}))  
        self.assertContains(response, '4') 

