from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth
from sign.models import Event,Guest
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        if username == '' or password == '':
            return render(request,"index.html",{"error":"username or password null !"})

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect('/event_manage/')
            request.session['username'] = username
            return response
        else:
            return render(request,"index.html",{"error":"username or password error!"})

@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user":username,"events":event_list})
