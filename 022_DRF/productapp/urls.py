from django.urls import path
from productapp.views import *

urlpatterns = [

        path("all",ProductView.as_view()),
        path("all/<id>",ProductViewRetrive.as_view())
]