from django.core.management.base import BaseCommand
from shop.views import ensure_demo_products
from shop.models import Product


class Command(BaseCommand):
    help = 'Creates demo products for the diploma project catalog.'

    def handle(self, *args, **options):
        before = Product.objects.count()
        ensure_demo_products()
        after = Product.objects.count()
        self.stdout.write(self.style.SUCCESS(f'Demo catalog ready. Products before: {before}, after: {after}.'))
