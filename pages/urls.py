from django.urls import path, re_path
from .views import PageListView, PageDetailView

app_name = 'pages'

urlpatterns = [
    path('', PageListView.as_view(), name='page-list'),
    re_path(r'^(?P<slug>[\w-]+(/[\w-]+)*)/$', PageDetailView.as_view(), name='page-detail'),
]
