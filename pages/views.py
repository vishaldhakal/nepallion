from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Page
from .serializers import PageSerializer

# Create your views here.

class PageListView(generics.ListAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PageDetailView(generics.RetrieveAPIView):
    queryset = Page.objects.filter(is_active=True)
    serializer_class = PageSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]
