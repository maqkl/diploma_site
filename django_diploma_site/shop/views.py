from decimal import Decimal
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import ContactForm, RegistrationForm
from .models import Product


def ensure_demo_products():
    """Creates demo catalog data when the project is empty."""

    if Product.objects.exists():
        return

    products = [
        {
            'name': 'NovaBook Air 14',
            'category': 'laptops',
            'short_description': 'Лёгкий ноутбук для учёбы, работы и поездок.',
            'description': '14-дюймовый ноутбук с быстрым SSD, тихой системой охлаждения и автономностью до 10 часов.',
            'price': Decimal('699.00'),
            'image': 'shop/img/product_laptop.svg',
            'rating': Decimal('4.8'),
        },
        {
            'name': 'Creator Station 16',
            'category': 'laptops',
            'short_description': 'Мощная рабочая станция для графики и программирования.',
            'description': 'Ноутбук с дискретной графикой, 16 GB RAM и экраном 16 дюймов для сложных проектов.',
            'price': Decimal('1299.00'),
            'image': 'shop/img/product_laptop_pro.svg',
            'rating': Decimal('4.9'),
        },
        {
            'name': 'DeskHub Mini PC',
            'category': 'laptops',
            'short_description': 'Компактный компьютер для дома и офиса.',
            'description': 'Мини-ПК с низким энергопотреблением, быстрым Wi-Fi и поддержкой двух мониторов.',
            'price': Decimal('449.00'),
            'image': 'shop/img/product_pc.svg',
            'rating': Decimal('4.7'),
        },
        {
            'name': 'Silent Mouse Pro',
            'category': 'accessories',
            'short_description': 'Беспроводная мышь с тихими кнопками.',
            'description': 'Эргономичная мышь с USB-C зарядкой, 3 режимами DPI и мягким кликом.',
            'price': Decimal('39.00'),
            'image': 'shop/img/product_mouse.svg',
            'rating': Decimal('4.6'),
        },
        {
            'name': 'TypeMaster Keyboard',
            'category': 'accessories',
            'short_description': 'Клавиатура для программирования и набора текста.',
            'description': 'Механическая клавиатура с подсветкой, сменными колпачками и компактной раскладкой.',
            'price': Decimal('89.00'),
            'image': 'shop/img/product_keyboard.svg',
            'rating': Decimal('4.8'),
        },
        {
            'name': 'Travel Dock 8-in-1',
            'category': 'accessories',
            'short_description': 'Док-станция для ноутбука с HDMI и USB-C.',
            'description': 'Портативная док-станция с HDMI, кардридером, Ethernet и быстрой зарядкой.',
            'price': Decimal('59.00'),
            'image': 'shop/img/product_dock.svg',
            'rating': Decimal('4.5'),
        },
        {
            'name': 'Установка Windows и драйверов',
            'category': 'services',
            'short_description': 'Подготовка компьютера к работе за один день.',
            'description': 'Установка системы, драйверов, браузера, архиватора, офисного пакета и базовой защиты.',
            'price': Decimal('35.00'),
            'image': 'shop/img/service_setup.svg',
            'rating': Decimal('4.9'),
        },
        {
            'name': 'Чистка ноутбука',
            'category': 'services',
            'short_description': 'Обслуживание охлаждения и замена термопасты.',
            'description': 'Разборка, удаление пыли, диагностика температур, замена термопасты и проверка нагрузки.',
            'price': Decimal('45.00'),
            'image': 'shop/img/service_cleaning.svg',
            'rating': Decimal('4.8'),
        },
        {
            'name': 'Настройка сайта на Django',
            'category': 'services',
            'short_description': 'Базовая настройка проекта, шаблонов и админ-панели.',
            'description': 'Создание структуры проекта, подключение моделей, URL, шаблонов, статических файлов и базы.',
            'price': Decimal('120.00'),
            'image': 'shop/img/service_django.svg',
            'rating': Decimal('5.0'),
        },
        {
            'name': 'Резервное копирование данных',
            'category': 'services',
            'short_description': 'Перенос и сохранение важных файлов пользователя.',
            'description': 'Копирование документов, фото и настроек на внешний носитель или в облачное хранилище.',
            'price': Decimal('30.00'),
            'image': 'shop/img/service_backup.svg',
            'rating': Decimal('4.7'),
        },
    ]
    Product.objects.bulk_create(Product(**item) for item in products)


def home(request):
    ensure_demo_products()
    products = Product.objects.all()[:6]
    return render(request, 'shop/home.html', {'products': products})


def about(request):
    return render(request, 'shop/about.html')


def catalog(request):
    ensure_demo_products()
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '').strip()
    products = Product.objects.all()

    # Server-side filtering is used together with the live JS filter.
    if query:
        products = products.filter(
            Q(name__icontains=query) |
            Q(short_description__icontains=query) |
            Q(description__icontains=query)
        )
    if category:
        products = products.filter(category=category)

    categories = Product.CATEGORY_CHOICES
    favorites_ids = [int(item) for item in request.session.get('favorites', [])]
    return render(request, 'shop/catalog.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'category': category,
        'favorites_ids': favorites_ids,
    })


def cart(request):
    cart_data = request.session.get('cart', {})
    items = []
    total = Decimal('0.00')

    for product_id, quantity in cart_data.items():
        product = get_object_or_404(Product, id=int(product_id))
        line_total = product.price * int(quantity)
        total += line_total
        items.append({'product': product, 'quantity': int(quantity), 'line_total': line_total})

    return render(request, 'shop/cart.html', {'items': items, 'total': total})


def favorites(request):
    ensure_demo_products()
    favorite_ids = request.session.get('favorites', [])
    products = Product.objects.filter(id__in=favorite_ids)
    return render(request, 'shop/favorites.html', {'products': products})


def contacts(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение успешно отправлено. Мы свяжемся с вами по Email.')
            return redirect('contacts')
        messages.error(request, 'Проверьте поля формы. Email должен быть корректным.')
    else:
        form = ContactForm()
    return render(request, 'shop/contacts.html', {'form': form})


def docs(request):
    return render(request, 'shop/docs.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация выполнена. Вы вошли в аккаунт.')
            return redirect('home')
        messages.error(request, 'Регистрация не выполнена. Исправьте ошибки в форме.')
    else:
        form = RegistrationForm()
    return render(request, 'shop/register.html', {'form': form})


@require_POST
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_data = request.session.get('cart', {})
    key = str(product.id)
    cart_data[key] = int(cart_data.get(key, 0)) + 1
    request.session['cart'] = cart_data
    messages.success(request, f'«{product.name}» добавлен в корзину.')
    return redirect(request.POST.get('next', 'catalog'))


@require_POST
def remove_from_cart(request, product_id):
    cart_data = request.session.get('cart', {})
    cart_data.pop(str(product_id), None)
    request.session['cart'] = cart_data
    messages.success(request, 'Позиция удалена из корзины.')
    return redirect('cart')


@require_POST
def clear_cart(request):
    request.session['cart'] = {}
    messages.success(request, 'Корзина очищена.')
    return redirect('cart')


@require_POST
def toggle_favorite(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    favorites = [int(item) for item in request.session.get('favorites', [])]
    if product.id in favorites:
        favorites.remove(product.id)
        messages.success(request, f'«{product.name}» удалён из избранного.')
    else:
        favorites.append(product.id)
        messages.success(request, f'«{product.name}» добавлен в избранное.')
    request.session['favorites'] = favorites
    return redirect(request.POST.get('next', 'catalog'))
