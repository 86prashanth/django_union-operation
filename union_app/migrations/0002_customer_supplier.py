# Generated by Django 4.1.1 on 2022-10-20 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('union_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=200)),
                ('customer_contact_number', models.CharField(max_length=200)),
                ('customer_country', models.CharField(max_length=200)),
                ('customer_city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Supplier_name', models.CharField(max_length=100)),
                ('Supplier_contact_name', models.CharField(max_length=100)),
                ('Supplier_country', models.CharField(max_length=100)),
                ('Supplier_city', models.CharField(max_length=100)),
            ],
        ),
    ]