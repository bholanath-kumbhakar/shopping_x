from store.models import AddtoCart, Category, Product, Wishlist

def all_cat(request):
    obj=Category.objects.all()
    if request.user.is_authenticated:
        obj2= Wishlist.objects.filter(user=request.user).first()
        count=obj2.product.all().count()

        obj3=AddtoCart.objects.filter(user=request.user).first()
        if obj3:
            cart_count= obj3.product.all().count()
        else:
            cart_count=0
    else:
        count=0
        cart_count=0

    return {'categories':obj,'count':count,'cart_count':cart_count}
        

    