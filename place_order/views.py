from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from products.models import Product
from bag.views import remove_item
from .forms import MakePaymentForm,OrderForms
from .models import OrderLineItem
from django.conf import settings
import stripe 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def get_bag_item_and_total(bag):
    
    
    grd_total=0
    bag_items = []
    for product_id, sizes in bag.items():
        
        product = get_object_or_404(Product, pk=product_id)
        for size,quantity in sizes.items():
        
        # print(quantity)
    
            bag_items.append({
                'id': product.id,
                'name': product.name,
                'brand': product.brand,
                'sku': product.sku,
                'size':size,
                'description': product.description,
                'image': product.image,
                'price': product.price,
                'stock': product.stock,
                'quantity': quantity,
                'total': product.price * quantity,
                
            }) 
            grd_total+=product.price * quantity
    return {'bag_items': bag_items,'grd_total':grd_total}  
    

@login_required
def place_order(request):
   
    bag = request.session.get('bag', {})
    bag_item_and_total=get_bag_item_and_total(bag)
    payment_form=MakePaymentForm()
    order_form = OrderForms()
    context={'payment_form':payment_form,'order_form':order_form,'publishable':settings.STRIPE_PUBLISHABLE_KEY}
    context.update(bag_item_and_total)
    return render(request, "place_order/place_order.html",context)
    
def remove_item_order(request,id):
    size=request.POST['size']
    bag=request.session.get('bag',{})
    del bag[str(id)][size]
    request.session['bag']=bag
    return redirect("place_order")
    
def submit_payment(request):
    
    bag = request.session.get('bag', {})
    bag_item_and_total=get_bag_item_and_total(bag)
    
    payment_form=MakePaymentForm(request.POST)
    form=OrderForms(request.POST)
    
    if form.is_valid() and payment_form.is_valid():
         #Saves the order to the DB
        order = form.save()
        bag = request.session.get('bag', {})
        for product_id, sizes in bag.items():
            for size, quantity in sizes.items():
                line_item = OrderLineItem()
                line_item.product_id = product_id
                line_item.size=size
                line_item.quantity = quantity
                line_item.order = order
                line_item.save()
        
        # Grab the money and run
        total = bag_item_and_total['grd_total']
        stripe_token=payment_form.cleaned_data['stripe_id']

        try:

            total_in_cent = int(total*100)
            customer = stripe.Charge.create(
                amount=total_in_cent,
                currency="EUR",
                description="Dummy Transaction",
                card=stripe_token,
            )

        except stripe.error.CardError:
            print("Declined")
            messages.error(request, "Your card was declined!")

        if customer.paid:
            print("Paid")
            messages.error(request, "You have successfully paid")
         
         #clear the cart       
        del request.session['bag']
        
        return redirect("/")
        