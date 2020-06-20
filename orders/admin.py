from django.contrib import admin
from orders.models import Pizza_style, Size, Pizza, Topping, Sub, Sub_type, Pasta,Pasta_type,PastaProtein, Salad, Platter, Platter_type, Cart

admin.site.register(Pizza)
admin.site.register(Pizza_style)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Sub_type)
admin.site.register(Pasta)
admin.site.register(Pasta_type)
admin.site.register(PastaProtein)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(Platter_type)
admin.site.register(Cart)

