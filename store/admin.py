from django.contrib import admin

from store.models import Address, AddtoCart, Category, Product, Size, Color, Wishlist, Order

# Register your models here.
@admin.register(Category)
class CategorymodelAdmin(admin.ModelAdmin):
    list_display=['name']
     

@admin.register(Product)
class ProductmodelAdmin(admin.ModelAdmin):
    list_display=['title','tag','description','price','image']

admin.site.register(Size)
admin.site.register(Color)
admin.site.register(Wishlist)
admin.site.register(AddtoCart)
admin.site.register(Order)

@admin.register(Address)
class AddressModelAdmin(admin.ModelAdmin):
    list_display=['user','address','pin','dist','state','country']

