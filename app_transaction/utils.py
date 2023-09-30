from .models import ProductInventories, TrxLines, Carts, Wishlists, Payment
from django.db.models import Q

def payment_checker(header_id):
    result = Payment.objects.filter(Q(is_paid=False) | Q(is_paid=None))\
            .filter(header=header_id)
    return False if result else True

def partial_update(instance, data):
    instance.fieldname = data.get("fieldname", instance.fieldname)
    instance.save()
    return instance

def stock_validation(product):
    stock = ProductInventories.objects.filter(id=product).values().first()
    
    orders = TrxLines.objects.filter(product_inv=product)
    calculate = lambda order: order["quantity"] if payment_checker(order["header_id"]) else 0
    qty_order = sum([calculate(order) for order in orders.values()])

    carts = Carts.objects.filter(product_inv=product)
    qty_cart = sum([data["quantity"] for data in carts])
    
    wishlists = Wishlists.objects.filter(product_inv=product)
    qty_wishlist = sum([data["quantity"] for data in wishlists])

    qty_available = stock["stock"] - qty_order - qty_cart - qty_wishlist
    return True if qty_available > 0  else False
        