from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        if data['Price'] <= 0:        
            raise serializers.ValidationError("Price must be greater than zero.")
        if data['Inventory'] < 0:
            raise serializers.ValidationError("Inventory cannot be negative.")
        return data
