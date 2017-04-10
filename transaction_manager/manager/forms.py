from django.contrib.auth.models import User
from django import forms
from .models import Transaction, Category

class RegisterForm(forms.ModelForm):

	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
	confirmation = forms.CharField(widget=forms.PasswordInput);

	class Meta:
		model = User
		fields = ['username', 'email', 'password']

	def clean(self):
		password = self.cleaned_data.get('password')
		confirmation = self.cleaned_data.get('confirmation')

		if password and password != confirmation:
			self.add_error("password", "Passwords don't match.")


class TransactionForm(forms.ModelForm):

	name = forms.CharField()
	class Meta:
		model = Transaction
		fields = ['name', 'value', 'category']


class CategoryForm(forms.ModelForm):

	class Meta:
		model = Category
		fields = ['name']
