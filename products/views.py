from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage
from django.contrib import messages
from .choices import price_choice, location_choice
from django.db.models import Q
from .models import Product
from orders.models import Order

# Create your views here.


def index(request):
    products = Product.objects.order_by(
        '-release_date').filter(is_released=True)
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paginated_products = paginator.get_page(page)
    context = {
        'products': paginated_products,
        'location': location_choice
    }
    return render(request, 'products/products.html', context)


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
        'prices': price_choice,
        'location': location_choice
    }
    return render(request, 'products/product.html', context)


def search(request):
    query_list = Product.objects.all().order_by('-release_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            query_list = query_list.filter(
                Q(description__icontains=keywords) | Q(color__icontains=keywords))
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            query_list = query_list.filter(location__icontains=location)
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            query_list = query_list.filter(price__lte=price)
    context = {
        'values': request.GET,
        'products': query_list,
        'prices': price_choice,
        'locations': location_choice,
    }
    return render(request, 'products/search.html', context)


def trace(request):
    if request.method == 'POST':
        phone = request.POST['phoneNo']
        phone = int(phone)
        phone = str(phone)
        if len(phone) < 10:
            messages.error(request, "Invalid Phone No.")
            return render(request, 'products/trace.html')
        else:
            query = Order.objects.filter(
                phone__icontains=phone).order_by('-order_date')
            context = {
                'orders': query,
                'phone': request.POST['phoneNo'],
            }
            return render(request, 'products/trace.html', context)
    else:
        return render(request, 'products/trace.html')
