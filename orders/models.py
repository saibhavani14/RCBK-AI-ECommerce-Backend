from django.db import models
from users.models import User

class Order(models.Model):
    STATUS = (
    ('Processing', 'Processing'),
    ('Packed', 'Packed'),
    ('Shipped', 'Shipped'),
    ('Out For Delivery', 'Out For Delivery'),
    ('Delivered', 'Delivered'),
)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id}"