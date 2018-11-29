def items_in_bag(request):
    bag=request.session.get('bag',{})
    count=0
    for quantity in bag.values():
        count+=quantity
    
    return {'items_in_bag':count}