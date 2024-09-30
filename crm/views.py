from django.shortcuts import render, get_object_or_404
from .models import Customer

def index(request):
    return render(request, 'crm/index.html')

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'crm/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'crm/customer_detail.html', {'customer': customer})

