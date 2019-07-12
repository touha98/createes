from django.shortcuts import render, redirect
from .models import Order
from products.models import Product
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.
def order(request):
    if request.method == 'POST':
        product_id = request.POST['product_id']
        name = request.POST['name']
        roll = request.POST['roll']
        dept = request.POST['dept']
        txnid = request.POST['txnid']
        size = request.POST['size']
        units = request.POST['units']
        payMethod = request.POST['payMethod']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        agent_email = request.POST['agent_email']
        product = Product.objects.get(pk=product_id)
        price = product.price * int(units)
        has_ordered = Order.objects.all().filter(txnid = txnid)
        if has_ordered : 
            messages.error(request, "You have already requested inquery for this product")
            return redirect('/products/' + product_id)
        else:
            order = Order(
                product = product, 
                product_id=product_id, 
                name=name, 
                email = email, 
                phone = phone, 
                message = message, 
                user_id = user_id,
                price = price,
                roll = roll,
                dept = dept,
                txnid = txnid,
                size = size,
                units = units,
                payMethod = payMethod)
            order.save()
            send_mail(
                "T-shirt order",
                "there has been an order for " + product.title + " by " + name,
                'createesbd@gmail.com',
                [agent_email,],
                fail_silently=False
            )
            
            messages.success(request, "Your order has been submitted for review. Check email or user dashboard for order status")
            return redirect('/products/' + product_id)