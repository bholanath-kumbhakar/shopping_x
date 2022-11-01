from django import template

register = template.Library()

@register.filter
def total_price(products):
    total = 0
    for i in products:
        total += i.price
    return total

@register.filter
def final_amount(products, delivery_charge=0, discount=5):
    total = 0
    for i in products:
        total += i.price

    discount_amount = (discount*total)/100
    discounted_price = (total-discount_amount)
    total_price = discounted_price + delivery_charge
    return total_price