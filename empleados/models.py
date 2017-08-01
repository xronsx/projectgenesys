#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Empleado(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	cedula = models.CharField(unique=True, max_length=255)
	direccion = models.CharField(max_length=600)
	tlf = models.CharField(max_length=255)
	color = models.CharField(max_length=255, unique=True)
	foto = models.ImageField(upload_to = 'profiles/')
	fecha_admision = models.DateTimeField('fecha admision', auto_now_add = False)

	def __str__(self):
		return str ((self.user.first_name)+" "+(self.user.last_name))