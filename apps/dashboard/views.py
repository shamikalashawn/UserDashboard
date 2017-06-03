#dashboard
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from ..LogReg.models import userDB
from .models import Message, Comment
# Create your views here.

#displays home page
def home(request):
    return render(request, 'dashboard/home.html')

#displays registration page
def registration(request):
    return render(request, 'dashboard/registration.html')

#displays log in page
def sign_in(request):
    return render(request, 'dashboard/sign_in.html')

#determines if user is admin or not then displays appropriate dashboard page
def dashboard(request):
    context = {
        'users': userDB.objects.all(),
        'remove': False,
    }
    if request.session['user']['user_level'] == 'admin':
        return render(request, 'dashboard/dashboard_admin.html', context)
    else:
        return render(request, 'dashboard/dashboard.html', context)

#shows a confirmation div on the admin dashboard before removing a user
def show(request, id):
    context = {
        'users': userDB.objects.all(),
        'remove': True,
        'del_user': userDB.objects.get(id=id)
    }
    return render(request, 'dashboard/dashboard_admin.html', context)

#hides confirmation div on the admin dashboard
def hide(request):
    context = {
        'users': userDB.objects.all(),
        'remove': False,
    }
    return render(request, 'dashboard/dashboard_admin.html', context)


#confirms admin is attempting to remove then removes user whose id has been passed in through urls
def remove(request, id):
    if request.session['user']['user_level'] == 'admin':
        userDB.objects.get(id=id).delete()
        return redirect('dashboard:dashboard')

#confirms admin is attempting to access then displays create new user page
def new_user(request):
    if request.session['user']['user_level'] == 'admin':
        return render(request, 'dashboard/new.html')
    else:
        return redirect('dashboard:dashboard')

#add new user method
def add_user(request):
    if request.method == 'POST':
        print "attempting to add a new user"
        response = userDB.objects.check_create(request.POST)
        if not response[0]:
            print 'error!'
            for error in response[1]:
                messages.error(request, error[1])
            return redirect('dashboard:new_user')
    return redirect('dashboard:dashboard')

#confirms admin is attempting to access then displays admin edit page for user with id
def edit_admin(request, id):
    if request.session['user']['user_level'] == 'admin':
        context = {
            'user': userDB.objects.get(id=id)
        }
        return render(request, 'dashboard/edit_admin.html', context)
    return redirect('dashboard:dashboard')

#validates information and updates user accordingly
def edit_info(request, id):
    if request.method == 'POST':
        response = userDB.objects.check_info_edit(request.POST, id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            if request.POST['page'] == 'admin':
                return redirect('dashboard:edit_admin', id=id)
            else:
                return redirect('dashboard:profile')
    return redirect('dashboard:dashboard')

#validates password and pswd conf then updates user accordingly
def edit_password(request, id):
    if request.method == 'POST':
        response = userDB.objects.check_pwd_edit(request.POST, id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
            if request.POST['page'] == 'admin':
                return redirect('dashboard:edit_admin', id=id)
            else:
                return redirect('dashboard:edit_profile')
    return redirect('dashboard:dashboard')

#validates description then updates user
def edit_description(request, id):
    if request.method == 'POST':
        response = userDB.objects.check_desc_edit(request.POST, id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
                return redirect('dashboard:edit_profile')
                return redirect('dashboard:dashboard')

#display profile page for user if there is a user in session
def profile(request):
    if 'user' in request.session:
        return render(request, 'dashboard/profile.html')
    return redirect('dashboard:home')

#display user page with their messages and comments
def show_user(request, id):
    owner = userDB.objects.get(id=id)
    context = {
        'owner': owner,
        'all_messages': Message.objects.filter(owner=owner),
        'comments': Comment.objects.filter(owner=owner),
    }
    return render(request, 'dashboard/user.html', context)

def message(request, owner_id):
    if request.method == "POST":
        author = userDB.objects.get(id=request.session['user']['id'])
        response = Message.objects.message_check(request.POST, owner_id, author)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
    return redirect('dashboard:show_user', id=owner_id)

def comment(request, owner_id, message_id):
    if request.method == "POST":
        author = userDB.objects.get(id=request.session['user']['id'])
        response = Comment.objects.comment_check(request.POST, owner_id, author, message_id)
        if not response[0]:
            for error in response[1]:
                messages.error(request, error[1])
    return redirect('dashboard:show_user', id=owner_id)
