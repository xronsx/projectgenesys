# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .models import *

@login_required(login_url = '/login/')
def nuevo_empleado(request, template_name = "empleados/nuevo_empleado.html"):
	return render(request, template_name, locals(),)