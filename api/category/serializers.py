from rest_framework import serializers

from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category # Model to be serialized
        fields = ('name', 'description') # Fields to be serialized