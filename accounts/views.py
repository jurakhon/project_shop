from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Student
from django.template import loader


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

# class MyTestPage(TemplateView):
#     template_name = "test.html"

def TestView(request):
    students = Student.objects.all()
    return render(request,"test.html",context={"students":students})





