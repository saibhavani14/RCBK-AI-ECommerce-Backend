import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
django.setup()

from products.models import Product

images = {
    "OnePlus 12R": "https://m.media-amazon.com/images/I/717JX3femML.jpg",
    "Redmi Note 13 Pro": "https://m.media-amazon.com/images/I/71VW8LmqqPL.jpg",
    "HP Pavilion": "https://m.media-amazon.com/images/I/71f5Eu5lJSL.jpg",
    "Dell Inspiron": "https://m.media-amazon.com/images/I/71TPda7cwUL.jpg",
    "Asus Vivobook": "https://m.media-amazon.com/images/I/71S8U9VzLTL.jpg",
    "Hair Dryer": "https://m.media-amazon.com/images/I/61la31UlZoL._AC_UF1000,1000_QL80_.jpg",
    "Face Wash": "https://rukmini1.flixcart.com/image/1500/1500/xif0q/face-wash/k/m/f/200-anti-dullness-brightening-facewash-100-grm-2-unit-ponds-original-imah2xargmejfdqb.jpeg?q=70",
    "Skin Care Kit": "https://m.media-amazon.com/images/I/61eA9PkZ07L.jpg",
    "Perfume": "https://m.media-amazon.com/images/I/61D4Z3yKPAL.jpg",
    "Men T-Shirt": "https://images-static.nykaa.com/media/catalog/product/0/d/0ddaba4USTSHC0084_1.jpg?tr=w-500",
    "Jeans": "https://m.media-amazon.com/images/I/71r09Sv-YLL._AC_UY1100_.jpg",
    "Jacket": "https://m.media-amazon.com/images/I/91bjXgpbspL._AC_UY1100_.jpg",
    "Sneakers": "https://m.media-amazon.com/images/I/71oEKkghg-L.jpg",
    "Power Bank": "https://m.media-amazon.com/images/I/61s+OTDUsKL._AC_UF1000,1000_QL80_.jpg",
    "USB Cable": "https://m.media-amazon.com/images/I/61DXuyMr6AL.jpg",
    "Mobile Cover": "https://m.media-amazon.com/images/I/61xYerZEYFL._AC_UF1000,1000_QL80_.jpg",
    "Gaming Mouse": "https://m.media-amazon.com/images/I/61UxfXTUyvL.jpg",
    "Gaming Keyboard": "https://m.media-amazon.com/images/I/71fRP7KY9hL.jpg",
    "Gaming Headset": "https://m.media-amazon.com/images/I/61CGHv6kmWL.jpg",
    "PS5 Controller": "https://m.media-amazon.com/images/I/61Q1Pa4X4-L.jpg",
    "Noise Smart Watch": "https://m.media-amazon.com/images/I/61akt30bJsL.jpg",
    "Boat Wave": "https://m.media-amazon.com/images/I/61DZclqQ4RL._AC_UF1000,1000_QL80_.jpg",
    "Fire-Boltt Ninja": "https://m.media-amazon.com/images/I/61ZjlBOp+rL.jpg",
    "Samsung Watch 6": "https://m.media-amazon.com/images/I/61ZjlBOp+rL.jpg",
    "Mixer Grinder": "https://m.media-amazon.com/images/I/51WEkopDGsL._AC_UF894,1000_QL80_.jpg",
    "Air Fryer": "https://m.media-amazon.com/images/I/61bK6PMOC3L.jpg",
    "Vacuum Cleaner": "https://m.media-amazon.com/images/I/51-NgiUucAL._AC_UF894,1000_QL80_.jpg",
    "Water Purifier": "https://m.media-amazon.com/images/I/71n3hlMPGeL._AC_UF1000,1000_QL80_.jpg",
}

for name, image in images.items():
    Product.objects.filter(name=name).update(image=image)

print("Product images updated successfully")
