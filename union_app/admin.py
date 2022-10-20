from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['Firstname','lastname','position','age']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['customer_name','customer_contact_number','customer_country','customer_city']
    
@admin.register(Supplier)   
class SupplierAdmin(admin.ModelAdmin):
    list_display=['Supplier_name','Supplier_contact_name','Supplier_country','Supplier_city']
    