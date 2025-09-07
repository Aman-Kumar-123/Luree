
from django.urls import path
from .views import Home,Cart,About

urlpatterns = [
    path('', Home,name='home'),
    path('cart',Cart,name='shopcart'),
    path('about',About,name='about'),  
]
