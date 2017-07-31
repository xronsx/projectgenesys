#-*- coding: utf-8 -*-
from django.db import models

class Empleado(models.Model):
	cedula = models.IntegerField(primary_key=True, unique=True)
	nombre = models.CharField(max_length=255)
	apellido = models.CharField(max_length=255)
	alias = models.CharField(max_length=255)
	direccion = models.CharField(max_length=600)
	tlf = models.CharField(max_length=255)
	color = models.CharField(max_length=255)
	email = models.EmailField()
	foto = models.ImageField(upload_to = 'profiles/', default = '/profiles/no_image.png')
	fecha_admision = models.DateTimeField('fecha admision', auto_now_add = False)

	def __str__(self):
		return str ((self.nombre)+" "+(self.apellido))