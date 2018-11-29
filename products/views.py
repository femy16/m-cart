from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductAdd_Form
# Create your views here.
def product_list(request):
    product=Product.objects.all()
    user=request.user
    # return render(request,"products/product_list.html")
    return render(request,"products/product_list.html",{'product':product,'user':user})
    
def product_details(request,id):
    product=Product.objects.get(pk=id)
    # reviews=Review.objects.filter(product_id=id)
    return render(request, "products/product_details.html",{'product':product})
    
def product_add(request):
    if request.method=="POST":
         form = ProductAdd_Form(request.POST,request.FILES)
         form.save()
         return redirect(product_list)
    else:
        form=ProductAdd_Form()
        return render(request,"products/product_add.html",{'form':form})