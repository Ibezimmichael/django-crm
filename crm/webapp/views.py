from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, CreateCustomerForm, UpdateCustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import Customer

def home(request):
    return  render(request, 'webapp/index.html')


# register

def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    context = {'form':form}
    return render(request, 'webapp/register.html', context=context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
    context = {'form':form}
    return render(request, 'webapp/login.html', context=context)

# - Dashboard

@login_required(login_url='login')
def dashboard(request):

    customers = Customer.objects.all()

    context = {'customers': customers}

    return render(request, 'webapp/dashboard.html', context=context)

@login_required(login_url='login')
def create_customer(request):
    form = CreateCustomerForm()
    if request.method == "POST":
        form = CreateCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your customer was created!")
            return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/create-customer.html', context=context)


# - Update a record 

@login_required(login_url='login')
def update_customer(request, pk):
    record = Customer.objects.get(id=pk)
    form = UpdateCustomerForm(instance=record)
    if request.method == 'POST':
        form = UpdateCustomerForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your customer was updated!")
            return redirect("dashboard")      
    context = {'form':form}
    return render(request, 'webapp/update-customer.html', context=context)


# - Read / View a singular record

@login_required(login_url='login')
def single_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {'customer':customer}
    return render(request, 'webapp/view-customer.html', context=context)


# - Delete a record

@login_required(login_url='login')
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    customer.delete()
    messages.success(request, "Your customer was deleted!")
    return redirect("dashboard")






#logout
def logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("login")