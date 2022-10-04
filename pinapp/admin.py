from django.contrib import admin
from .models import Address


@admin.register(Address)
class AdminModel(admin.ModelAdmin):
    list_display = ['id','name','description','pincode','city','state', 'country']