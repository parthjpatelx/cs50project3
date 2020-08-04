from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from orders.models import Pizza_style, Pizza, Size, Cart, OrderStatus
from django.contrib.auth.decorators import login_required


def index(request):
    # style_objects = Pizza_style.objects.all()
    # style_names = []
    # for style in style_objects:
    #     name = style.__dict__['style']
    #     style_names.append(name)

    # context = {
    #     'pizza_styles': style_names
    # }
    # return render(request, "orders/menu.html", context)

    serialized = []
    for pizza in Pizza.objects.all(): 
        pie = pizza.__dict__
        item = {'type': Pizza_style.objects.get(pk=pie['type_id']), 
                'toppings':pie['toppings'], 
                'size':Size.objects.get(pk=pie['size_id']),
                'price': pie['price'],
                'id' : pie['id']}
        serialized.append(item)
    context = {
        'pizzas': serialized
    }

    return render(request, "orders/menu.html", context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "orders/login.html", {"message": "Invalid credentials."})
    else:
        return render(request, "orders/login.html")

def logout_view(request):
      logout(request)
      return render(request, "orders/login.html", {"message": "Logged out."})

def register(request):
    # note: add error pages so that users are not to debug page in case an exception is made (i..e if passwords dont match, django inherent form validation)
    if request.method == 'POST':
        try:
            username = request.POST["username"]
            password = request.POST["password"]
            password_again = request.POST["password_again"]
            email = request.POST["email"]
        except KeyError:
            return render(request, "orders/error.html", {"message": "Please enter all required fields"})
        
        if password != password_again:
            # return render(request, "orders/error.html", {"message": "Passwords must match"})
            raise ValidationError('passwords must match')    

        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)

        return HttpResponseRedirect(reverse("index"))
    else: 
        return render(request, "orders/register.html")


def add_item(request):
    if request.method == 'POST':

        if not request.user.is_authenticated:
            return render(request, "orders/error.html", {"message": "You must be logged in to do this"})

        pizza = Pizza.objects.get(pk=request.POST["pizza_id"])
        current_user = request.user
        pending = OrderStatus.objects.get(status='pending')
        
        try:
            current_cart = Cart.objects.get(user=current_user, status=pending)
        except:
            current_cart = Cart(user=current_user, status=pending)
            current_cart.save()
        
        current_cart.pizza.add(pizza)
        current_cart.save()
        
        pizzas = current_cart.pizza

        return render(request, "cart.html", {'pizzas' : pizzas})
            
    else:
        return render(request, "orders/error.html", {"message": "This path only accepts POST requests"})


