from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/',views.SignIn.as_view(),name='signin'),
    path('signup/',views.SignUp.as_view(),name='signup'),
    path('signout',views.SignOut.as_view(),name='signout'),
    path('',views.HomeView.as_view(),name='home'),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
    path('productview/<int:id>',views.ProductView.as_view(),name='productview'),
    path('add_wishlist/',views.WishlistView.as_view(),name='wishlist'),
    path('editprofile/<int:id>',views.EditProfile.as_view(),name='editprofile'),
    path('address/',views.AddressView.as_view(),name='address'),
    path('add_address/',views.AddAddressView.as_view(),name='add_address'),
    path('add_cart/',views.AddtocartView.as_view(),name='addtocart'),
    path('placeorder/',views.PlaceOrder.as_view(),name='placeorder'),
    path('orderplaced/',views.OrderPlaced.as_view(),name='orderplaced'),
    path('showorder',views.ShowOrder.as_view(),name='showorder')
]
