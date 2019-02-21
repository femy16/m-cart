"""mcart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from accounts.views import signup,show_profile
from products.views import product_list,product_details,product_add,select_category,product_edit,product_delete,home_page,home_brand
from bag.views import add_to_bag,view_bag,remove_item
from place_order.views import place_order,submit_payment
from reviews.views import make_review
from django.views.static import serve
from django.conf import settings
urlpatterns = [
    path('media/<path:path>',serve,{'document_root':settings.MEDIA_ROOT}),
    path('',home_page,name="home_page"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/signup/', signup, name='signup'),
    path('accounts/profile', show_profile, name='show_profile'),
    path('product_details/<int:id>',product_details,name='product_details'),
    path('product_add/',product_add,name='product_add'),
    path('bag/add',add_to_bag,name='add_to_bag'),
    path('bag/view_bag',view_bag,name='view_bag'),
    path('bag/remove,<int:id>',remove_item,name='remove_item'),
    path('placeorder/',place_order,name='place_order'),
    path('placeorder/pay',submit_payment,name='submit_payment'),
    path('product_details/reviews/<int:id>',make_review,name='make_review'),
    path('product/category/<int:id>',select_category,name='select_category'),
    path('product/brand/<str:cat>',home_brand,name='home_brand'),
    path('product_edit/<int:id>',product_edit,name='product_edit'),
    path('product_delete/<int:id>',product_delete,name='product_delete')
    
]
