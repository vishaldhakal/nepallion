from rest_framework import serializers
from .models import Page

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'slug', 'content', 'meta_description', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
