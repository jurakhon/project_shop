from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class MyHomePage(TemplateView):
    template_name = "home.html"

# Create your views here.
class MyLoginPage(TemplateView):
    template_name = "login.html"

class MyRegisterPage(TemplateView):
    template_name = "register.html"

class MyCartPage(TemplateView):
    template_name = "cart.html"

class MyProductsPage(TemplateView):
    template_name = "products.html"

class MyOrdersPage(TemplateView):
    template_name =  "orders.html"

class MyLogoutPage(TemplateView):
    template_name = "logout.html"

class MyCheckOutPage(TemplateView):
    template_name = "checkout.html"

