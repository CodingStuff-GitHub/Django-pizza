from django import forms 

class PizzaForm(forms.Form):
    pizza_type = forms.CharField(max_length=10, 
        widget=forms.TextInput(
            attrs={}))
    pizza_size = forms.CharField(max_length=10, 
        widget=forms.TextInput(
            attrs={}))
    pizza_toppings = forms.CharField(max_length=50, 
        widget=forms.TextInput(
            attrs={}))
