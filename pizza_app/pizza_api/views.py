from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Pizza
from .forms import PizzaForm

def index(request):
    pizza_list = Pizza.objects.order_by('id')

    form = PizzaForm()

    context = {'pizza_list' : pizza_list, 'form' : form}

    return render(request, 'pizza/index.html', context)

@require_POST
def addPizza(request):
    form = PizzaForm(request.POST)

    if form.is_valid():
        new_pizza = Pizza(pizza_type=request.POST['pizza_type'], 
        	pizza_size=request.POST['pizza_size'], 
        	pizza_toppings=request.POST['pizza_toppings'])
        new_pizza.save()

    return redirect('index')