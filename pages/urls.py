from django.urls import path
from .views import PagesListView, PagesDetailView, PagesCreateView

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    path('create/', PagesCreateView.as_view(), name='create'),
], 'pages')