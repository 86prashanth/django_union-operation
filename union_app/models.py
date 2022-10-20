from django.db import models 

class Employee(models.Model):
    Firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    position=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    
    def __str__(self):
        return "%s%s%s%s "%(self.Firstname,self.lastname,self.position,self.age)

class Customer(models.Model):
    customer_name=models.CharField(max_length=200)
    customer_contact_number=models.CharField(max_length=200)
    customer_country=models.CharField(max_length=200)
    customer_city=models.CharField(max_length=200)
    def __str__(self):
        return "%s%s%s%s" %(self.customer_name,self.customer_contact_number,self.customer_city,self.customer_country)

class Supplier(models.Model):
    Supplier_name=models.CharField(max_length=100)
    Supplier_contact_name=models.CharField(max_length=100)
    Supplier_country=models.CharField(max_length=100)
    Supplier_city=models.CharField(max_length=100)
    def __str__(self):
        return '%s%s%s%s' %(self.Supplier_name,self.Supplier_contact_name,self.Supplier_country,self.Supplier_city)