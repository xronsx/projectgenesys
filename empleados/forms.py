#-*- coding: utf-8 -*-
from django import forms
from empleados.models import *
from django.forms.fields import DateField
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import *
from django.conf import settings
from django.forms import ModelChoiceField
from django.core.files import File

Colector = "Colector"
Administrador = "Administrador"
GRUPO = (
        (Colector, 'Colector'),
        (Administrador, 'Administrador'),
    )

class NuevoEmpleado(forms.Form):
	username = forms.CharField(label = "Alias", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias'}))
	email = forms.EmailField(label = "Email", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(label = "Contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	nombre =  forms.CharField(label = "Nombre", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	apellido =  forms.CharField(label = "Apellido", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
	grupo = ModelChoiceField(label = "Grupo", required = True, queryset=Group.objects.all(), initial=2, widget = forms.Select(attrs={'class': 'form-control'}))
	cedula = forms.CharField(label = "Cédula", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula', 'data-mask':'99.999.999'}))
	direccion = forms.CharField(label = "Dirección", widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
	tlf = forms.CharField(label = "Tlf", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'data-mask': '(9999) 999-9999)'}))
	color =  forms.CharField(label = "demo_apidemo", required = True, widget = forms.TextInput(attrs={'class': 'form-control demo1 btn btn-w-m btn-warning back-change', 'placeholder': 'Seleccione un color', 'id':'demo_apidemo'}))
	fecha = forms.DateField(label = "Fecha", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM-DD-AA'}))
	foto = forms.FileField(label='foto', required = True)

	def __init__(self, *args, **kwargs):
		super(NuevoEmpleado, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}

class NuevoEmpleado_editar(forms.Form):
	username = forms.CharField(label = "Alias", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Alias'}))
	email = forms.EmailField(label = "Email", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(label = "Contraseña", required = True, widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
	nombre =  forms.CharField(label = "Nombre", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
	apellido =  forms.CharField(label = "Apellido", required = True, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}))
	grupo = ModelChoiceField(label = "Grupo", required = True, queryset=Group.objects.all(), initial=2, widget = forms.Select(attrs={'class': 'form-control'}))
	cedula = forms.CharField(label = "Cédula", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cédula', 'data-mask':'99.999.999'}))
	direccion = forms.CharField(label = "Dirección", widget = forms.Textarea(attrs={'class': 'form-control', 'rows': '5'}))
	tlf = forms.CharField(label = "Tlf", widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono', 'data-mask': '(9999) 999-9999)'}))
	color =  forms.CharField(label = "demo_apidemo", required = True, widget = forms.TextInput(attrs={'class': 'form-control demo1 btn btn-w-m btn-warning back-change', 'placeholder': 'Seleccione un color', 'id':'demo_apidemo'}))
	fecha = forms.DateField(label = "Fecha", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM-DD-AA'}))
	foto = forms.FileField(label='foto')

	def __init__(self, *args, **kwargs):
		super(NuevoEmpleado_editar, self).__init__(*args, **kwargs)
		# Errores predeterminados definidos en el modelo este disparará errores para campo requerido, unico, invalido y con caracterers faltantes
		for field in self.fields.values():
			field.error_messages = {'required':'Ingrese {fieldname}'.format(
				fieldname=field.label), 'unique':'{fieldname} registrada en el sistema'.format(
				fieldname=field.label), 'invalid':'Valor Inválido'.format(
				fieldname=field.label), 'min_length':'Realice completacion de campo {fieldname}'.format(
				fieldname=field.label)}