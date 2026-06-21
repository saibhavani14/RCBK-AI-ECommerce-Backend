import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from products.models import Category, Product

products = [
    ("OnePlus 12R", "OnePlus Gaming Phone", 42999, 60, "Mobiles"),
    ("Redmi Note 13 Pro", "Redmi 5G Smartphone", 24999, 70, "Mobiles"),

    ("HP Pavilion", "HP Laptop", 58999, 15, "Electronics"),
    ("Dell Inspiron", "Dell Productivity Laptop", 54999, 18, "Electronics"),
    ("Asus Vivobook", "Asus Laptop", 49999, 25, "Electronics"),

    ("Hair Dryer", "Professional Hair Dryer", 1299, 30, "Beauty"),
    ("Face Wash", "Daily Face Wash", 299, 100, "Beauty"),
    ("Skin Care Kit", "Complete Skin Care Kit", 1499, 40, "Beauty"),
    ("Perfume", "Premium Perfume", 999, 50, "Beauty"),

    ("Men T-Shirt", "Cotton T-Shirt", 599, 100, "Fashion"),
    ("Jeans", "Slim Fit Jeans", 1499, 80, "Fashion"),
    ("Jacket", "Winter Jacket", 2499, 30, "Fashion"),
    ("Sneakers", "Casual Sneakers", 1999, 40, "Fashion"),

    ("Power Bank", "20000mAh Power Bank", 1299, 60, "Accessories"),
    ("USB Cable", "Fast Charging Cable", 299, 120, "Accessories"),
    ("Mobile Cover", "Shockproof Mobile Cover", 199, 150, "Accessories"),

    ("Gaming Mouse", "RGB Gaming Mouse", 999, 80, "Gaming"),
    ("Gaming Keyboard", "Mechanical Keyboard", 2499, 50, "Gaming"),
    ("Gaming Headset", "Surround Sound Headset", 1999, 45, "Gaming"),
    ("PS5 Controller", "Wireless Controller", 5999, 20, "Gaming"),

    ("Noise Smart Watch", "AMOLED Smart Watch", 2999, 60, "Smart Watches"),
    ("Boat Wave", "Fitness Smart Watch", 2499, 70, "Smart Watches"),
    ("Fire-Boltt Ninja", "Sports Smart Watch", 1999, 50, "Smart Watches"),
    ("Samsung Watch 6", "Premium Smart Watch", 24999, 10, "Smart Watches"),

    ("Mixer Grinder", "Kitchen Mixer", 3499, 25, "Home Appliances"),
    ("Air Fryer", "Healthy Cooking Appliance", 4999, 20, "Home Appliances"),
    ("Vacuum Cleaner", "Portable Vacuum Cleaner", 5999, 15, "Home Appliances"),
    ("Water Purifier", "RO Water Purifier", 8999, 10, "Home Appliances"),
]

for name, desc, price, stock, cat_name in products:
    category, created = Category.objects.get_or_create(name=cat_name)

    Product.objects.get_or_create(
        name=name,
        defaults={
            "description": desc,
            "price": price,
            "stock": stock,
            "category": category,
        },
    )

print("Products added successfully")