from django.urls import path,include
from myapp.views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('categories', CategoryViewset)
router.register('products', ProductViewset)
router.register('users',UserViewset)
router.register('address',AddressViewset)
router.register('carts', CartViewset,basename="carts")

urlpatterns = [
    path('', include(router.urls)),
    
    path("payment",payment,name="payment")
]