from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, TransactionForm, CategoryForm
from .models import Transaction, Category

def index(request) :
	if not request.user.is_authenticated():
		return redirect('/manager/log_in/')

	transactions = Transaction.objects.filter(user=request.user)
	return render(request, 'manager/index.html', {'transactions': transactions})


def log_in(request):
	
	if request.method != "POST":
		return render(request, 'manager/log_in.html')
		
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(username=username, password=password)

	if user is None:
		return render(request, 'manager/log_in.html', {'error_message': 'Invalid login/password.'})

	login(request, user)
	
	return index(request)

def log_out(request):
    logout(request)
    return redirect('/manager/log_in/')

def register(request):
	form = RegisterForm(request.POST or None)

	if form.is_valid():

		user = form.save(commit=False)

		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user.set_password(password)

		user.save()

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return index(request)

	return render(request, 'manager/register.html', {'form': form})


def add_transaction(request):
	if not request.user.is_authenticated():
		return redirect('/manager/log_in/')

	form = TransactionForm(request.POST or None)

	if form.is_valid():
		trans = form.save(commit=False)
		trans.user = request.user
		trans.save()
		return index(request)

	return render(request, 'manager/add_transaction.html', {'form': form})

def categories(request):
	if not request.user.is_authenticated():
		return redirect('/manager/log_in/')

	categories = Category.objects.all()
	return render(request, 'manager/categories.html', {'categories': categories})


def add_category(request):
		
	if not request.user.is_authenticated():
		return redirect('/manager/log_in/')

	form = CategoryForm(request.POST or None)

	if form.is_valid():
		category = form.save(commit=False)
		category.save()
		return categories(request)

	return render(request, 'manager/add_category.html', {'form': form})
