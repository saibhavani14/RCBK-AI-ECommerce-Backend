from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import RegisterSerializer, UserListSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from products.models import Product
from orders.models import Order
from django.db.models import Sum
token_generator = PasswordResetTokenGenerator()
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "mobile": request.user.mobile
        })


class UserListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserListSerializer



class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            reset_link = f"{settings.FRONTEND_URL}/reset-password?uid={uid}&token={token}"

            send_mail(
                "RCBK Password Reset",
                f"Click this link to reset your password:\n{reset_link}",
                settings.DEFAULT_FROM_EMAIL,
                [email],
                fail_silently=False,
            )

            return Response({
                "message": "Password reset link sent to email"
            })

        except User.DoesNotExist:
            return Response({
                "error": "User with this email does not exist"
            }, status=404)


class ResetPasswordView(APIView):
   
    def post(self, request):
    
        uid = request.data.get("uid")
        token = request.data.get("token")
        password = request.data.get("password")
        

        try:
            user_id = urlsafe_base64_decode(uid).decode()
            user = User.objects.get(pk=user_id)

            if token_generator.check_token(user, token):
                user.set_password(password)
                user.save()

                return Response({
                    "message": "Password reset successful"
                })

            return Response({
                "error": "Invalid or expired token"
            }, status=400)

        except Exception:
            return Response({
                "error": "Invalid reset request"
            }, status=400)
        

class AdminStatsView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        total_products = Product.objects.count()
        total_orders = Order.objects.count()
        total_users = User.objects.count()

        revenue = Order.objects.aggregate(
            total=Sum("total_amount")
        )["total"] or 0

        return Response({
            "products": total_products,
            "orders": total_orders,
            "users": total_users,
            "revenue": revenue
        })