from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from learn.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def index(request):
    pass
    return render(request, 'index.html')


# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)   # 登录
        # if username == 'admin' and password == 'admin123':
            # return HttpResponse('登录成功！')
            # return HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)    # 添加浏览器cookie
            request.session['user'] = username  # 读取浏览器session
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})


# 发布会管理
@login_required
def event_manege(request):
    event_list = Event.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get("name", "")
    print(username)
    print(search_name)
    event_list = Event.objects.filter(name__contains=search_name)
    print(event_list)
    return render(request, "event_manage.html", {"user": username, "events": event_list})


# 嘉宾管理
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    # print(guest_list)
    paginator = Paginator(guest_list, 5)                                                    # 创建每页5条数据的分页器
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username, "guests": contacts})


# 嘉宾手机号搜索
@login_required
def search_guest(request):
    username = request.session.get('user', '')
    # guest_list = Guest.objects.all()
    # print(search_guest)
    # print(username)
    # print(search_name)
    search_phone = request.GET.get("phone", "")
    # search_name_bytes = search_phone.encode(encoding="utf-8")                              # 这句不用加了
    # search_guest = request.GET.get("realname", "")
    # print(search_guest)
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    print(guest_list)
    paginator = Paginator(guest_list, 5)                                                    # 创建每页5条数据的分页器
    print(paginator)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    print(guest_list)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": contacts,
                                                 "phone": search_phone})


# 签到页面
@login_required
def sign_index_action(request, eid):
    event = get_object_or_404(Event, id=eid)
    phone = request.POST.get('phone', '')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'phone error.'})
    result = Guest.objects.filter(phone=phone, event_id=eid)
    if not result:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'event id or phone error.'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event, 'hint': 'user has signed in..'})
    else:
        Guest.objects.filter(phone=phone, event_id=eid).update(sign='1')
        return render(request, 'sign_index.html', {'event': event, 'hint': 'sign in.success.', 'guest': result})


# 退出函数
@login_required
def logout(request):
    auth.logout(request)                            # 退出登录
    response = HttpResponseRedirect('/index/')
    return response
