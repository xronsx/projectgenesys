# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_view(request):
	state = ""
	username = ""
	password = ""
	next = ""

	if request.GET:
	    next = request.GET['next']

	if request.POST:
	    username = request.POST['username']
	    password = request.POST['password']

	    if '@' in username:
	        try:
	            check = User.objects.get(email=username)
	            username = check.username
	        except:
	            pass

	    user = authenticate(username=username, password=password)
	    if user is not None:
	        if user.is_active:
	            login(request, user)
	            if next == "":
	                return HttpResponseRedirect('/home/')
	            else:
	                return HttpResponseRedirect(next)
	        else:
	            state = 0
	    else:
	        state = 0
	return render(request, 'inicio/login.html', {'state':state, 'username': username, 'next': next,},)

@login_required(login_url = '/login/')
def login_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url = '/login/')
def home(request, template_name = "inicio/dashboard.html"):
	return render(request, template_name, locals(),)