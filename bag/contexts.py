def items_in_bag(request):
    bag=request.session.get('bag',{})
    count=0
    
    
    for product, sizes in bag.items():
        for quantity in sizes:
            count+=sizes[quantity]
    # for quantity in bag.values():
    #     count+=quantity
        
    # for quantity in bag[1]['M']:
    #     print(quantity)
    #     count+=quantity    
    
    return {'items_in_bag':count}
    