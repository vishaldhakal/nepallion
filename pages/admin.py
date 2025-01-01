from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Page
from tinymce.widgets import TinyMCE

@admin.register(Page)
class PageAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'is_active', 'created_at', 'updated_at']
    list_filter = ['is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'content', 'meta_title', 'meta_description']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'is_active')
        }),
        ('Content', {
            'fields': ('content',),
            'classes': ('wide',)
        }),
        ('SEO Settings', {
            'fields': ('meta_title', 'meta_description'),
            'description': 'Search engine optimization settings for better visibility in search results.'
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            kwargs['widget'] = TinyMCE()
        return super().formfield_for_dbfield(db_field, **kwargs)