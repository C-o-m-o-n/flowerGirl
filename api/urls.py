from django.urls import path
from . import views

urlpatterns = [
    path('all-flowers', views.getFlowers, name="all-flowers"),
    path('categories', views.getCategories, name="categories"),
    path('user-details', views.getUserDetails, name="user-details"),
    path('users', views.getUsers, name="users"),
    
    # path('orders', views.getOrders, name="orders"),
    # path('carts', views.getCart, name="carts"),
    # path('wishlist', views.getWishlist, name="wishlist"),
]