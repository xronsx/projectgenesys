# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from datetime import datetime, timedelta
from django.db import IntegrityError

@login_required(login_url = '/login/')
def nuevo_empleado(request, template_name = "empleados/nuevo_empleado.html"):
	if request.method == 'POST':
		form = NuevoEmpleado(request.POST, request.FILES)
		fecha = request.POST['fecha']
		print(fecha)
		if form.is_valid():
			alias = request.POST['username']
			contra = request.POST['password']
			nombre = request.POST['nombre']
			apellido = request.POST['apellido']
			grupo = request.POST['grupo']
			email = request.POST['email']
			# capturar error
			try:
				new_user = User.objects.create_user(username = alias, password = contra, first_name = nombre, last_name=apellido, email=email)
			except IntegrityError as e:
				error = "Usuario ya regitrado"
				return render(request, template_name, locals(),)
			if new_user:
				group = Group.objects.get(pk=grupo)
				new_user.groups.add(group)
				user_extras = Empleado(user = User.objects.get(username = new_user.username), cedula = request.POST['cedula'], direccion = request.POST['direccion'], tlf = request.POST['tlf'], color = request.POST['color'], fecha_admision = request.POST['fecha'], foto = request.FILES['foto'])
				user_extras.save()
				if user_extras:
					exito = "OK"
					form = NuevoEmpleado()
				else:
					print("noooooo")
			else:
				print("ERROR")
		else:
			print(form.errors)
	else:
		form = NuevoEmpleado()
		# form.fields['fecha'].initial = datetime.now().strftime("%m-%d-%y")
	return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def profiles(request, template_name = "empleados/profiles.html"):
	# usuarios = Empleado.objects.all().exclude(username = 'admin')
	usuarios = User.objects.all().exclude(username = 'admin')
	empleados = Empleado.objects.all()
	return render(request, template_name, locals(),)

@login_required(login_url = '/login/')
def profile(request, id_emp, template_name = "empleados/profile.html"):
	usuario = User.objects.get(pk = id_emp)
	persona = Empleado.objects.get(user = usuario)
	print(persona)
	return render(request, template_name, locals(),)