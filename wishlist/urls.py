from django.urls import path
from .views import WishlistListCreateView, WishlistDetailView

urlpatterns = [
    path('wishlist/', WishlistListCreateView.as_view()),
    path('wishlist/<int:pk>/', WishlistDetailView.as_view()),
]