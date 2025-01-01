from django.db import models
from django.utils.text import slugify
from tinymce.models import HTMLField

class Page(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    content = HTMLField()
    
    # SEO Fields
    meta_title = models.CharField(
        max_length=60, 
        blank=True,
        help_text="The title that appears in search engine results (max 60 characters)"
    )
    meta_description = models.TextField(
        max_length=160,
        blank=True,
        help_text="A brief description that appears in search engine results (max 160 characters)"
    )
    
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.meta_title:
            self.meta_title = self.title[:60]  # Use first 60 chars of title if meta_title not provided
        super().save(*args, **kwargs)