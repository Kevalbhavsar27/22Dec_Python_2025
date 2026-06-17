from django.contrib import admin
from productapp.models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Address)