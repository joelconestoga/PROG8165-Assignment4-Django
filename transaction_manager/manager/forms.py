from django.contrib.auth.models import User
from django import forms

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

