from rest_framework import viewsets
from .serializers import CategorySerializer
from .models import Category

# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at') # Operations to be performed
    serializer_class = CategorySerializer # Class responsible for serializing the data
