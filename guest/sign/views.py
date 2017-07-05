from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required



# Create your views here.
# 首页(登录)
def index(request):
    return render(request, "index.html")


# 登录动作
def login_action(request):
    print(request.method)
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get(' password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = username
            response = HttpResponseRedirect('/event_manage/')
            print(type(response))
            #response.set_cookie('user',username, 3600)
            return  response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

@login_required
def event_manage(request):
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user":username})
    #username = request.COOKIES.get('user', '')
    #return render(request,"event_manage.html",{"user":username})
    #return render(request,"event_manage.html")
    #event_list = Event.objects.all()
    #username = request.session.get('username', '')
    #return render(request, "event_manage.html", {"user": username, "events": event_list})
'''
# 退出登录
@login_required
def logout(request):
    # del request.session['username']
    auth.logout(request)  # 退出登录
    response = HttpResponseRedirect('/index/')
    return response


# 发布会管理（登录之后默认页面）
@login_required
'''



