from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Contact, Comment
from .serializers import ProductSerializer, ContactSerializer, CommentSerializer
# Create your views here.


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


def home(request):
    return render(request, 'index.html', {})
