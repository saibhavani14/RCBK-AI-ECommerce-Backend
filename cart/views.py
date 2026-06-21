from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Cart
from .serializers import CartSerializer


class CartListCreateView(generics.ListCreateAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        return Cart.objects.all()

    def perform_create(self, serializer):
        serializer.save(user_id=1)


class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def get_queryset(self):
        return Cart.objects.all()