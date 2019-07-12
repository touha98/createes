from django.shortcuts import render
from products.choices import price_choice, location_choice
from products.models import Product
from agent.models import Agent

# Create your views here.
def index(request):
    products = Product.objects.order_by('-release_date').filter(is_released = True)[:3]
    context = {
        'products': products,
        'prices': price_choice,
        'locations': location_choice
    }
    return render(request, 'pages/index.html', context)

def about(request):
    agent = Agent.objects.all()
    context={
        'agents': agent
    }
    return render(request, 'pages/about.html', context)