from django.urls import path
from .views import AISearchView

urlpatterns = [
    path('ai/search/', AISearchView.as_view(), name='ai-search'),
]