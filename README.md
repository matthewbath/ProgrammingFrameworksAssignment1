# Flashcards Project

## Overview

This project contains a flash cards system that allows users to create, browse, and study flashcard sets. It includes:
- Create flashcard sets
- View flashcard sets
- Study flashcards and click to reveal answers
- Mark flashcards as hidden 

The backend is built with Django, and the frontend interface allows users to interact with flashcards using basic HTML and JavaScript.

## Features

- **Flashcard Sets**: You can create multiple flashcard sets and also add cards to them.
- **Interactive Study Mode**: Users can study flashcards, revealing answers by clicking on "reveal answer".
- **Flashcard Visibility**: Users can hide certain flashcards, which will not be shown to them when studying.
- **Admin Interface**: An admin interface allows the management of flashcard sets and cards.

## Installation

### Prerequisites

1. Python 3.x
2. Django 5.x

### Steps to Set Up

1. Clone the repository:
   Using CMD, put in the following commands:
   git clone https://github.com/matthewbath/ProgrammingFrameworksAssignment1.git
   cd flashcards-project

2. Install dependencies:
   pip install -r requirements.txt

3. Run migrations:
   python manage.py migrate

4. Create a superuser for admin access (optional but recommended for managing flashcards):
   python manage.py createsuperuser

5. Run the development server:
   python manage.py runserver

6. Visit the site at http://127.0.0.1:8000/flashcard_sets/ in your browser
