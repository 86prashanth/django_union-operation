from http.client import HTTPResponse
from django.shortcuts import render
from .models import *
from django.http import HttpResponse
# Create your views here.
def home(request):
    queryset=Employee.objects.filter(age__gt=28)
    print(queryset)
    queryset2=Employee.objects.filter(Firstname='prashanth')
    print(queryset2)
    result=queryset.union(queryset2)
    queryset3=Customer.objects.filter(customer_country='uk')
    queryset4=Supplier.objects.filter(Supplier_country='uk')
    union=queryset3.union(queryset4)
    return HttpResponse({'result':result,'union':union})