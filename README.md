# Book_Management_API

## Overview

The Book Management API is a Django REST Framework (DRF) based API for managing a collection of books. It provides endpoints for creating, reading, updating, and deleting book records.

## Features

- List all books
- Retrieve details of a specific book
- Create a new book
- Update an existing book
- Delete a book

## Setup

### Prerequisites

- Python 3.x 
- Django 3.x
- Django REST Framework

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url> /path/to/your/folder
   cd /path/to/your/folder
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv virtualenv
   source virtualenv/bin/activate  # On Windows use `virtualenv\Scripts\activate`
   ```

3. Install the required packages:
   bash
   pip install -r requirements.txt
   

4. Apply migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   

5. Run the development server:
   ```bash
   python manage.py runserver
   ```
   

## Usage

### List all books

- **URL:** `/api/books/`
- **Method:** `GET`
- **Response:**
  json
  [
      {
          "id": 1,
          "Title": "The Great Gatsby",
          "author": "F. Scott Fitzgerald",
          "Price": "10.99",
          "Inventory": 5
      },
      ...
  ]
  

### Retrieve a specific book

- **URL:** `/api/books/<int:pk>/`
- **Method:** `GET`
- **Response:**
  json
  {
      "id": 1,
      "Title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "Price": "10.99",
      "Inventory": 5
  }
  

### Create a new book

- **URL:** `/api/books/`
- **Method:** `POST`
- **Request Body:**
  json
  {
      "Title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "Price": "10.99",
      "Inventory": 5
  }
  
- **Response:**
  json
  {
      "id": 1,
      "Title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "Price": "10.99",
      "Inventory": 5
  }
  ```

### Update an existing book

- **URL:** `/api/books/<int:pk>/`
- **Method:** `PUT`
- **Request Body:**
  json
  {
      "Title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "Price": "12.99",
      "Inventory": 10
  }
  ```
- **Response:**
  json
  {
      "id": 1,
      "Title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald",
      "Price": "12.99",
      "Inventory": 10
  }
  

### Delete a book

- **URL:** `/api/books/<int:pk>/`
- **Method:** `DELETE`
- **Response:
  json
  {
      "message": "Book deleted successfully"
  }
  


