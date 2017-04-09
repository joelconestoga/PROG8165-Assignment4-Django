from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

# Create your views here.
def index(request) :
	return render(request, 'manager/index.html')


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
