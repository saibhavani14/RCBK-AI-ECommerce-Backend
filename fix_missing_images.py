import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from products.models import Product

default_images = {
    "Mobiles": "https://via.placeholder.com/300x300?text=Mobile",
    "Electronics": "https://via.placeholder.com/300x300?text=Electronics",
    "Beauty": "https://via.placeholder.com/300x300?text=Beauty",
    "Fashion": "https://via.placeholder.com/300x300?text=Fashion",
    "Accessories": "https://via.placeholder.com/300x300?text=Accessories",
    "Gaming": "https://via.placeholder.com/300x300?text=Gaming",
    "Smart Watches": "https://via.placeholder.com/300x300?text=Smart+Watch",
    "Home Appliances": "https://via.placeholder.com/300x300?text=Home+Appliance",
}

for product in Product.objects.all():
    if not product.image:
        product.image = default_images.get(
            product.category.name,
            "https://via.placeholder.com/300x300?text=Product"
        )
        product.save()

print("Missing product images fixed")