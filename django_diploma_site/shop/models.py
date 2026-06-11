from django.db import models


class Product(models.Model):
    """Product or service item shown in the catalog."""

    CATEGORY_CHOICES = [
        ('laptops', 'Ноутбуки'),
        ('accessories', 'Аксессуары'),
        ('services', 'Услуги'),
    ]

    name = models.CharField(max_length=120)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    short_description = models.CharField(max_length=220)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=120, default='shop/img/product_laptop.svg')
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.8)
    in_stock = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    """Message submitted from the contact form."""

    name = models.CharField(max_length=80)
    email = models.EmailField()
    topic = models.CharField(max_length=120)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} - {self.topic}'
