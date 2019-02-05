from django.contrib import admin
from .models import Customer, Wallet, Transaction

# Register your models here.

admin.site.register(Customer)
admin.site.register(Wallet)
admin.site.register(Transaction)
