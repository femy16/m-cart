from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from products.models import Product
import json
# Create your views here.
def add_to_bag(request):
    product_id=request.POST['product']
    quantity=int(request.POST['quantity'])
    # size=request.POST['size']
    bag= request.session.get('bag',{})
    bag[product_id]=bag.get(product_id,0)+quantity
    request.session['bag']=bag
    return redirect("/")
    
def view_bag(request):
    bag = request.session.get('bag', {})
    
    grd_total=0
    bag_items = []
    for product_id, quantity in bag.items():
        
        product = get_object_or_404(Product, pk=product_id)
        grd_total+=product.price * quantity
        # print(quantity)
    
        bag_items.append({
            'id': product.id,
            'name': product.name,
            'brand': product.brand,
            'sku': product.sku,
            'description': product.description,
            'image': product.image,
            'price': product.price,
            'stock': product.stock,
            'quantity': quantity,
            'total': product.price * quantity,
            
        })    
    

    return render(request,"bag/view_bag.html", {'bag_items': bag_items,'grd_total':grd_total})
def remove_item(request,id):
    bag=request.session.get('bag',{})
    del bag[str(id)]
    request.session['bag']=bag
    return redirect("view_bag")
    