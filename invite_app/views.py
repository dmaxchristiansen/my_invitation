from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.conf import settings
import bcrypt

def index(request):
    return render(request, "index.html")

def reg(request):
    return render(request, "reg.html")

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/reg")
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print(pw_hash)
        user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pw_hash)
        if user:
            request.session['userid']=user.id
            return redirect("/success")

def success(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, "success.html", context)

def login(request):
    user = User.objects.filter(email=request.POST['email'])
    if user:
        logged_user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['userid']=logged_user.id
            return redirect("/success")
    return redirect("/")

def logout(request):
    if 'userid' not in request.session:
        return redirect("/")
    else:
        del request.session['userid']
    return render(request, "logout.html")

def invite1(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, 'invite1.html', context)

def invite2(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, 'invite2.html', context)

def invite3(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, 'invite3.html', context)

def acceptInvite(request):
    return render(request, 'accept_invite.html')

def profile(request):
    if 'userid' not in request.session:
        return redirect("/")
    context = {
        "user": User.objects.get(id=request.session['userid']),
    }
    return render(request, 'profile.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

