from django.db import models

class Pizza(models.Model):
	pizza_type = models.CharField(max_length=10)
	pizza_size = models.CharField(max_length=10)
	pizza_toppings = models.CharField(max_length=50)
	
	def __str__(self):
		return self.pizza_type
