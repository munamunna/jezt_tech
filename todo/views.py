from django.shortcuts import render,redirect

# Create your views here.

# todo/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import ToDoItem
from todo.forms import LoginForm,TaskForm,RegistrationForm
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils.decorators import method_decorator


def signin_required(fn):
    def wrapper(request,*args,**kargs):
        if not request.user.is_authenticated:
            messages.error(request,"you must login to perform this action")
            return redirect("todo:login")
        return fn(request,*args,**kargs)
    return wrapper

class SignupView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("todo:login")

    def form_valid(self, form):
        messages.success(self.request,"account created")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"failed to create account")
        return super().form_invalid(form)

class SigninView(View):
    model=User
    template_name="login.html"
    form_class=LoginForm

    def get(self,request,*args,**kargs):
        form=self.form_class
        return render(request,self.template_name,{"form":form})
    
    def post(self,request,*args,**kargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            usname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=usname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,"login success")
                return redirect("todo:todo_list")
            messages.error(request,"invalid credential")
            return render(request,self.template_name,{"form":form})

class ToDoListView(ListView):
    model = ToDoItem
    template_name = 'todo_list.html'
    context_object_name = 'tasks'


@method_decorator(signin_required,name="dispatch")    
class ToDoCreateView(CreateView):
    model=ToDoItem
    form_class=TaskForm
    template_name="todo_add.html"
    success_url=reverse_lazy("todo:todo_create")

    #to add extra details in form before save
    def form_valid(self, form):
        form.instance.user=self.request.user
        
        messages.success(self.request,"todo has been created")
        return super().form_valid(form)