from django.shortcuts import render,redirect
from .models import Product
from .forms import ProductAdd_Form
from reviews.forms import ReviewForm
# Create your views here.

def home_page(request):
    return render(request,"products/home.html")
def product_list(request):
    product=Product.objects.all()
    user=request.user
    # return render(request,"products/product_list.html")
    return render(request,"products/product_list.html",{'product':product,'user':user})
    
def product_details(request,id):
    product=Product.objects.get(pk=id)
    # reviews=Review.objects.filter(product_id=id)
    form = ReviewForm()
    return render(request, "products/product_details.html",{'product':product,'form':form})
    
def product_add(request):
    if request.method=="POST":
         form = ProductAdd_Form(request.POST,request.FILES)
         form.save()
         return redirect(product_list)
    else:
        form=ProductAdd_Form()
        return render(request,"products/product_add.html",{'form':form})
        
def product_edit(request,id):
    product=Product.objects.get(pk=id)
    if request.method=="POST":
         form = ProductAdd_Form(request.POST,request.FILES, instance=product)
         form.save()
         return redirect("/product_details/{0}".format(id))
    else:
        form=ProductAdd_Form(instance=product)
        return render(request,"products/product_add.html",{'form':form})
        
def product_delete(request,id):
    
    Product.objects.filter(id=id).delete()
    return redirect(product_list)
         
def select_category(request,id):
    
    product=Product.objects.filter(productcategories_id=str(id))
    user=request.user
    # return render(request,"products/product_list.html")
    return render(request,"products/product_list.html",{'product':product,'user':user})
    