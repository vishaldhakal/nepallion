from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Page
from .serializers import PageSerializer
from django.urls import re_path
from rest_framework.exceptions import NotFound

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
    
    def get_object(self):
        """
        Override to handle nested slugs with slashes
        """
        slug = self.kwargs.get('slug', '')
        
        # Try to find the page with the exact slug (which may contain slashes)
        try:
            return Page.objects.get(slug=slug, is_active=True)
        except Page.DoesNotExist:
            raise NotFound(f"No active page found with slug: {slug}")
