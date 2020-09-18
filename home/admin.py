from django.contrib import admin

# Register your models here.
from home.models import products,contact
admin.site.register(products)
admin.site.register(contact)