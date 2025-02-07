from django.urls import path, include
from . import views

urlpatterns = [
    path('activity-detail/<str:slug>/', views.activities_single),
    path('activities/', views.activities_collection),
    path('activities-slug/', views.activities_slug),
    path('activities-search/', views.activities_search),
    path('activitiy-categories-slug/', views.activities_cat_slug),
    path('activities-regions/', views.activities_regions),
    path('activities-region-slug/', views.activities_reg_slug),
    path('destinations/', views.destinations_list, name='destinations_list'),
    path('destinations/detailed/', views.destinations_list_detailed, name='destinations_list_detailed'),
    path('destination/<str:slug>/', views.destination_detail, name='destination_detail'),
    path('activitiy-categories/', views.activity_categories_collection),
    path('activity-category/<str:slug>/', views.activity_category_detail),
    path('activities-all/<str:slug>/', views.activities_all),
    path('activities-region-wise/<str:slug>/', views.activities_all_region),
    path('activities-featured/', views.activities_featured),
    path('sign/', views.sign_view, name='sign_view'),
    
    # Checkout endpoints
    path('activity-checkouts/', views.activity_checkouts_collection),
    path('activity-checkout/<int:id>/', views.activity_checkout_single),
    path('activity-checkout/create/', views.activity_checkout_create),
    path('activity-checkout/update/<int:id>/', views.activity_checkout_update),
    path('activity-checkout/delete/<int:id>/', views.activity_checkout_delete),
    path('activities-autocomplete/', views.activity_autocomplete),
]
