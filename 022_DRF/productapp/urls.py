from django.urls import path
from productapp.views import *

urlpatterns = [

        path("products",ProductView.as_view()),
        path("products/<id>",ProductViewRetrive.as_view()),

        path("categories",CategoryView.as_view()),
        path("categories/<id>",CategoryViewRetrive.as_view()),

        path("products/category/<id>",product_by_category)
]