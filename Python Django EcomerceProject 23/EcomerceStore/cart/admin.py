from django.contrib import admin

# Register your models here.

from cart.models import Cart, Account, Order

admin.site.register(Cart)
admin.site.register(Account)
admin.site.register(Order)