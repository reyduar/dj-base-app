from django.urls import path
from .views import PagesListView, PagesDetailView, PagesSearchView

pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PagesDetailView.as_view(), name='page'),
    path('create/', PagesSearchView.as_view(), name='create'),
], 'pages')