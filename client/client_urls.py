from django.urls import path
from django.contrib import admin

import client
from client import client_views
from pgfinder import urls

urlpatterns = [
    path('main/', client_views.main),
    path('userlogin/', client_views.UserLogin),
    path('userforgot/', client_views.UserForgot),
    path('c_sendotp/', client_views.UserSendotp),
    path('c_pass/', client_views.UserPassword),
    path('c_register/', client_views.UserRegister),
    path('insert/', client_views.insertUser),
    path('shop/', client_views.shop),
    path('cart/', client_views.cart),

    path('product-details/<int:id>', client_views.product_details),
    path('ins-feed/', client_views.InsFeedback),
    path('list/', client_views.listing),
    path('contact/', client_views.contact),
    path('ins_enq/', client_views.ins_enquiry),
    path('myaccount/', client_views.account),
    path('userlogout/', client_views.UserLogout),
    path('booking/<int:id>', client_views.booking),
    path('date/<int:id>', client_views.open_date),
    path('change/', client_views.changePassword),
    path('update/', client_views.updateProfile),

    path('ownerlogin/', client_views.OwnerLogin),
    path('search_product/', client_views.autosuggest, name='pro_search'),
    path('searchp/', client_views.search),
    path('loc/<int:id>', client_views.location),
    path('wishlist/<int:id>', client_views.insert_wishlist),
    path('showwish/', client_views.show_wishlist),
    path('delwish/<int:id>', client_views.delete_wishlist),
    path('del_pgwish/<int:id>', client_views.del_pg_wish),
    path('ajax/load-cities/', client_views.sort_product, name='ajax_sort_products'),
    path('ajax_filter_products/', client_views.filter_product, name='ajax_filter_products'),
    path('filter_cat/', client_views.short_category),

    path('c_404/', client_views.error),
    path('filter/', client_views.filter),

    path('ownerforgot/', client_views.OwnerForgot),
    path('o_sendotp/', client_views.OwnerSendotp),
    path('o_pass/', client_views.OwnerPassword),
    path('o_register/', client_views.OwnerRegister),
    path('insert_o/', client_views.insertOwner),
    path('client_header_menu/', client_views.load_menu),

]
