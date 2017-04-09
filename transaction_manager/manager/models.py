from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Transaction(models.Model):
	user = models.ForeignKey(User, default=1)
	name = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=6, decimal_places=2)