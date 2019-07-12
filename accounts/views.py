from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.models import User
from orders.models import Order
from django.contrib.auth.password_validation import validate_password

# Create your views here.


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass_word = request.POST['password']
        user = auth.authenticate(username=email, password=pass_word)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'accounts/login.html')


def create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_2 = request.POST['password2']

        # check password match
        if password == password_2:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return redirect('create')
            else:
                user = User.objects.create_user(
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email)
                user.save()
                messages.success(
                    request, 'You are now registered and can login')
                return redirect('login')
        else:
            messages.error(request, "passwords do not match")
            return redirect('create')
    else:
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'accounts/register.html')


def dashboard(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user_id=request.user.id)
        context = {
            'orders': orders
        }
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('index')


def edit(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            userName = request.user.username
            password = request.POST['oldPass']
            new_password1 = request.POST['new_password_1']
            new_password2 = request.POST['new_password_2']
            auth_user = auth.authenticate(username=userName, password=password)
            if auth_user is not None:
                print(new_password1)
                print(new_password2)
                if new_password1 == new_password2:
                    if len(new_password1) < 8:
                        messages.error(
                            request, "Password must be 8 digits long")
                        return render(request, 'accounts/edit.html')
                    else:
                        user = User.objects.get(username=userName)
                        user.set_password(new_password1)
                        user.save()
                        messages.success(
                            request, "Password Changed Successfully")
                        return render(request, 'accounts/edit.html')
                else:
                    messages.error(request, "New password didn't match")
                    return render(request, 'accounts/edit.html')
            else:
                messages.error(request, "Password is incorrect!")
                return render(request, 'accounts/edit.html')
        else:
            return render(request, 'accounts/edit.html')
    else:
        return redirect('index')


def reset(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        return render(request, 'accounts/reset.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')
