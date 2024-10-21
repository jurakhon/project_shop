from django.urls import path
from .views import MyHomePage, MyRegisterPage, MyLoginPage, MyCartPage, MyProductsPage, MyOrdersPage, MyLogoutPage, MyCheckOutPage

urlpatterns = [
    path("", MyHomePage.as_view(), name="home"),
    path("register", MyRegisterPage.as_view(), name="register"),
    path("login", MyLoginPage.as_view(), name="login"),
    path("cart", MyCartPage.as_view(), name="cart"),
    path("products", MyProductsPage.as_view(), name="products"),
    path("orders", MyOrdersPage.as_view(), name="orders"),
    path("logout", MyLogoutPage.as_view(), name="logout"),
    path("checkout", MyCheckOutPage.as_view(), name="checkout"),



]