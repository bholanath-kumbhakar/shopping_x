
from http.client import HTTPResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib import messages
from.models import AddtoCart, Category, Product, Wishlist,Address,Order
from django.urls import reverse

# # Create your views here.

#signup view
 
class SignUp(View):

    def get(self,request):

        return render (request,'store/signup.html')

    def post(self,request):
        mob=request.POST.get('Phone_number')
        fn=request.POST.get('First_name')
        ln=request.POST.get('Last_name')
        em=request.POST.get('Email')
        ps=request.POST.get('Password')
        user = User.objects.create_user(username=mob,first_name=fn,last_name=ln,email=em, password=ps)
        user.save()
        messages.success(request,'account created successfully')
        return render (request,'store/home.html')




#signin view

class SignIn(View):
    
    def get(self,request):
         return render(request,'store/login.html')
    def post(self,request):
        un=request.POST.get('Phone_number')
        ps=request.POST.get('Password')
        user=authenticate(username=un,password=ps)
        if user is not None:
            login(request,user)
        return HttpResponseRedirect('/')


#signout view
@method_decorator(login_required,name="dispatch")
class SignOut(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect ('/')


#home view
class HomeView(View):
    def get(self,request):
        catagory = request.GET.get('category')
        if catagory:
            all_product=Product.objects.filter(category__name=catagory)
        else:
            all_product=Product.objects.all()
        context={'products':all_product}
        return render (request,'store/home.html',context)
  


#dashboard view
@method_decorator(login_required,name="dispatch")
class Dashboard(View):
    def get(self,request):
        return render(request,'store/dashboard.html')

#product View  
class ProductView(View):
    def get(self,request,id):
        product=Product.objects.filter(id=id).first()
        whish = Wishlist.objects.filter(user=request.user, product__in=[id])
        cart_obj=AddtoCart.objects.filter(user=request.user, product__in=[id])
        return render(request,'store/productdetails.html',{'item':product, 'whish':whish,'cart_obj':cart_obj})


#Add to cart view
class AddtocartView(View):
    def get(self,request):
        if request.user.is_authenticated:
            cart_obj=AddtoCart.objects.filter(user=request.user).first()
            return render(request,'store/addtocart.html',locals())
        else:
            return render(request,'store/addtocart2.html')
    
    def post(self,request):
        product_id=request.POST.get('product_id')
        cart_btn=request.POST.get('cart_remove')
        if cart_btn == 'remove':
            print("============")
            obj = AddtoCart.objects.filter(user=request.user).first()
            obj.product.remove(Product.objects.get(id=product_id))
            obj.save()
            return HttpResponseRedirect ('/add_cart/')
        else:
            obj=AddtoCart.objects.filter(user=request.user).first()
            if not obj:
                obj=AddtoCart(user=request.user)
                obj.save()
            obj.product.add(Product.objects.get(id=product_id))
            obj.save()
            return HttpResponseRedirect(reverse('productview', args=[product_id]))



#wishlist
class WishlistView(View):

    def get(self, request):
        if request.user.is_authenticated:
            wishlist_obj = Wishlist.objects.filter(user=request.user).first()
            return render(request,'store/wishlist.html', locals())
        else:
            return render(request,'store/wishlist2.html')

    def post(self,request):
        product_id = request.POST.get("product_id")
        wish_btn = request.POST.get("wish_btn")
        
        if wish_btn == 'remove':
            obj = Wishlist.objects.filter(user=request.user).first()
            obj.product.remove(Product.objects.get(id=product_id))
            obj.save()
            return HttpResponseRedirect ('/add_wishlist')
        else:

            obj = Wishlist.objects.filter(user=request.user).first()
            
            if not obj:
                obj = Wishlist(user=request.user)
                obj.save()
            obj.product.add(Product.objects.get(id=product_id))
            obj.save()
            
            return HttpResponseRedirect(reverse('productview', args=[product_id]))
            # return HttpResponseRedirect('/productview/')

#edit profile
class EditProfile(View):
    def get(self,request,id):
        user=User.objects.filter(id=id).first()
        return render(request,'store/editprofile.html')

    def post(self, request, id):
        fn=request.POST.get('First_name')
        ln=request.POST.get('Last_name')
        email=request.POST.get('Email')
        user=User.objects.get(id=id)
        user.first_name=fn
        user.last_name=ln
        user.email=email
        user.save()
        return HttpResponseRedirect ('/dashboard/')

#AddressView

class AddressView(View):
    def get(self,request):        
        ad_obj=Address.objects.filter(user=request.user)

        return render(request,'store/address.html',{'address':ad_obj})

    def post(self,request):
        id = request.POST.get('address_id')
        address = Address.objects.filter(id=id).first()
        address.delete()
        return HttpResponseRedirect('/address/')

#add addressview

class AddAddressView(View):

    def get(self,request):
        return render (request,'store/add_address.html' )

    def post(self,request):
        nm=request.POST.get('Name')
        mb=request.POST.get('Mobile')
        ad=request.POST.get('Address')
        pin=request.POST.get('Pin')
        dt=request.POST.get('Dist')
        st=request.POST.get('State')
        cn=request.POST.get('Country')
        address=Address.objects.create(user=request.user,name=nm,mobile=mb,address=ad,pin=pin,dist=dt,state=st,country=cn)
        address.save()
        return HttpResponseRedirect('/address/')


#place orer view

class PlaceOrder(View):
    def get(self,request):
        address=Address.objects.filter(user=request.user)
        return render(request,'store/placeorder.html',{'address':address})


    def post(self,request):
        ad=request.POST.get('checkbox')
        cod=request.POST.get('cod')
        online=request.POST.get('online')
        
        cart_product=AddtoCart.objects.filter(user=request.user).first()
        allproduct=cart_product.product.all()
        for product in allproduct:
            order=Order(user=request.user,product=product,address_id=ad,payment_type='COD')
            order.save()

        # cart_product.delete()
        return HttpResponseRedirect('/orderplaced/')

#order placed
class OrderPlaced(View):
    def get(self,request):
        return render(request,'store/thanks.html')



#show order

class ShowOrder(View):
    def get(self,request):
        order_obj=Order.objects.filter(user=request.user)

        return render(request,'store/showorder.html',{'order':order_obj})
