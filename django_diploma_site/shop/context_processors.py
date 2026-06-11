def site_counters(request):
    """Counters for cart and favorites in the navigation menu."""

    cart = request.session.get('cart', {})
    favorites = request.session.get('favorites', [])
    return {
        'cart_count': sum(int(qty) for qty in cart.values()),
        'favorites_count': len(favorites),
    }
