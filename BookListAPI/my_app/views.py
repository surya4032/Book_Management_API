from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponseBadRequest, QueryDict, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book
from django.shortcuts import get_object_or_404
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

class BookList(APIView):
    def get(self, request):
        try:
            books = Book.objects.all()
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            logging.error(f"Error fetching books: {e}")
            return Response({"error": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                logging.error(f"Error saving book: {e}")
                return Response({"error": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetails(APIView):
    def get(self, request, pk):
        logging.debug(f"GET request for book with id: {pk}")
        try:
            book = Book.objects.get(id=pk)
            logging.debug(f"Book found: {book}")
            serializer = BookSerializer(book)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Book.DoesNotExist:
            logging.error(f"Book with id {pk} not found")
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(f"Error fetching book with id {pk}: {e}")
            return Response({"error": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        logging.debug(f"PUT request for book with id: {pk}")
        try:
            book = Book.objects.get(id=pk)
            data = request.data
            serializer = BookSerializer(book, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            logging.error(f"Book with id {pk} not found")
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(f"Error updating book with id {pk}: {e}")
            return Response({"error": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({"message": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            logging.error(f"Book with id {pk} not found")
            return Response({"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            logging.error(f"Error deleting book with id {pk}: {e}")
            return Response({"error": "Server error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Configure logging
logging.basicConfig(level=logging.DEBUG)







