from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),   
    path("register", views.register, name="register"),   
    path("cart/add", views.add_item, name="add_item")   
    # path("cart/view/", views.view_cart, name="view_cart")   
]
