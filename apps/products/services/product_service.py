from apps.products.models.product import Product

def get_products_in_stock_min():
    return Product.objects.filter(stock__gt=2)
