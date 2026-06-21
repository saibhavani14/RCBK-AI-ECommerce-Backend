from rest_framework import generics
from rest_framework.permissions import AllowAny

from django.core.mail import EmailMessage
from django.conf import settings

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from io import BytesIO

from .models import Order
from .serializers import OrderSerializer
from users.models import User


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    def perform_create(self, serializer):
        order = serializer.save(user_id=1)

        user = User.objects.get(id=1)

        # Create PDF invoice in memory
        buffer = BytesIO()
        pdf = canvas.Canvas(buffer, pagesize=A4)

        pdf.setTitle(f"Invoice_{order.id}")

        pdf.setFont("Helvetica-Bold", 20)
        pdf.drawString(180, 800, "RCBK AI E-Commerce")

        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(240, 760, "Invoice")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 720, f"Invoice ID: INV-{order.id}")
        pdf.drawString(50, 700, f"Order ID: #{order.id}")
        pdf.drawString(50, 680, f"Customer Name: {user.username}")
        pdf.drawString(50, 660, f"Customer Email: {user.email}")
        pdf.drawString(50, 640, f"Order Status: {order.status}")
        pdf.drawString(50, 620, f"Order Date: {order.created_at}")

        pdf.line(50, 600, 550, 600)

        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, 570, "Payment Summary")

        pdf.setFont("Helvetica", 12)
        pdf.drawString(50, 545, f"Total Amount: Rs. {order.total_amount}")

        pdf.line(50, 520, 550, 520)

        pdf.setFont("Helvetica-Bold", 13)
        pdf.drawString(50, 490, "Thank you for shopping with RCBK!")

        pdf.save()

        buffer.seek(0)
        pdf_file = buffer.getvalue()
        buffer.close()

        subject = "RCBK Order Placed Successfully"

        message = f"""
Hello {user.username},

Your order has been placed successfully.

Order ID: #{order.id}
Total Amount: Rs. {order.total_amount}
Status: {order.status}

Your invoice PDF is attached with this email.

Thank you for shopping with RCBK AI E-Commerce.

Regards,
RCBK Team
"""

        email = EmailMessage(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
        )

        email.attach(
            f"Invoice_{order.id}.pdf",
            pdf_file,
            "application/pdf"
        )

        email.send(fail_silently=False)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]
    authentication_classes = []