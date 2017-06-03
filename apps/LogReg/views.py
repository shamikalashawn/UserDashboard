#LogReg
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import userDB

# Create your views here.

def log_reg(request):
    if request.method == "POST":
        if request.POST['attempt'] == "register":
            response = userDB.objects.check_create(request.POST)
        elif request.POST['attempt'] == 'login':
            response = userDB.objects.check_login(request.POST)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            if request.POST['attempt'] == "register":
                return redirect('dashboard:registration')
            elif request.POST['attempt'] == 'login':
                return redirect('dashboard:sign_in')
        else:
            request.session['user'] = {
                'first_name': response[1].first_name,
                'last_name' : response[1].last_name,
                'id': response[1].id,
                'user_level': response[1].user_level,
                'email': response[1].email,
            }
        return redirect('dashboard:dashboard')
    return redirect('dashboard:home')

def logout(request):
    request.session.clear()
    return redirect('dashboard:home')
