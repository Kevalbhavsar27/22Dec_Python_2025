from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth.models import User
from myapp.models import *
from myapp.serializer import *
from rest_framework import viewsets, status
from rest_framework.permissions import *
from rest_framework.decorators import action,api_view
from django.http import JsonResponse
import razorpay

def index(request):
    return  Response("done")


class CategoryViewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
       
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

class ProductViewset(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False, methods=['get'], url_path=r'categories/(?P<category_id>\d+)')
    def categories(self, request, category_id):
      
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def get_permissions(self):
       
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

class UserViewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    

class AddressViewset(viewsets.ModelViewSet):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
    def get_queryset(self):
        # Show only logged-in user's addresses
        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically save logged-in user
        serializer.save(user=self.request.user)

    def get_permissions(self):
       
        if self.action in ['create', 'update', 'partial_update', 'destroy','list','retrive']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
    
    
class CartViewset(viewsets.ModelViewSet):

    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only logged-in user's cart items
        return Cart.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):

        product_id = request.data.get('product')
        qty = int(request.data.get('qty', 1))

      

        cart_item = Cart.objects.filter(
            user=request.user,
            product_id=product_id
        ).first()

        if cart_item:
            c = cart_item.qty + qty
            
            if c>0:
                cart_item.qty = c
                cart_item.save()
            elif c<=0:
                
                cart_item.delete()
                return Response(
                {
                    "message": "Cart Deleted",
                },
                status=status.HTTP_200_OK
                )



            serializer = self.get_serializer(cart_item)

            return Response(
                {
                    "message": "Quantity updated in cart",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
            
            
        if qty <= 0:
            return Response(
                {
                    "error": "Quantity must be greater than 0"
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            {
                "message": "Product added to cart",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
        

@api_view(['POST'])
def payment(request):
    amt = int(request.data['amount'])
    client = razorpay.Client(auth=("rzp_test_SrVF3qKpUUSwRy", "cQWzjjQRmeAPudfjsoRJNX8i"))

    data = { "amount": amt*100, "currency": "INR", "receipt": "order_rcptid_11" }
    payment = client.order.create(data=data) # Amount is in currency subunits.
    return JsonResponse(payment)
