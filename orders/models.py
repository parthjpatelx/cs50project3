from django.db import models
from django.conf import settings


#Added
class Pizza_style(models.Model):
    style = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.style}'

class Size(models.Model):
    size = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f'{self.size}'

# cheese = 0 toppings
# special = 4 toppings

class Pizza(models.Model):
    type = models.ForeignKey(Pizza_style, on_delete=models.CASCADE, related_name='types')
    # set toppings to 0 if toppings are not specified
    toppings = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='sizes')
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f"Pizza type: {self.type}, Toppings: {self.toppings}, Size: {self.size}, Price: {self.price}"

class Topping(models.Model):
    topping = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.topping}'

#how to add extra cheese to a sub? Add an optional boolean?

class Sub_type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'

class Sub(models.Model):
    type = models.ForeignKey(Sub_type, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)
    # toppings = models.ManyToManyField(Toppings, blank=True)

    def __str__(self):
        return f'Type: {self.type}, Size = {self.size}, {self.price}'

    
class Pasta_type(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.name}'

class PastaProtein(models.Model):
    protein = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.protein}'

class Pasta(models.Model):
    name = models.ForeignKey(Pasta_type, on_delete=models.CASCADE)
    price = price = models.FloatField(max_length=4)
    protein = models.ForeignKey(PastaProtein, on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}, Protein: {self.protein}'


class Platter_type(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.type}'

class Platter(models.Model):
    name = models.ForeignKey(Platter_type, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f'Name: {self.name}, Size: {self.size}, Price: {self.price}'

class Salad(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(max_length=4)

    def __str__(self):
        return f'Name: {self.name}, Price: {self.price}'


class OrderStatus(models.Model):
    status = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.status}'

class Cart(models.Model):
    pizza= models.ManyToManyField(Pizza, blank=True)
    subs= models.ManyToManyField(Sub, blank=True)
    pasta= models.ManyToManyField(Pasta, blank=True)
    salads= models.ManyToManyField(Salad, blank=True)
    platters= models.ManyToManyField(Platter, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=999)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, default=1)
