from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from learn.models import Event, Guest, ProjectInfo, InterfaceInfo, InterfaceField
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
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


# 退出函数
@login_required
def logout(request):
    auth.logout(request)                            # 退出登录
    response = HttpResponseRedirect('/index/')
    return response


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
    search_realname = request.GET.get("realname", "")
    # search_name_bytes = search_phone.encode(encoding="utf-8")                              # 这句不用加了
    # search_guest = request.GET.get("realname", "")
    # print(search_guest)
    guest_list = Guest.objects.filter(phone__contains=search_phone)
    # guest_list = Guest.objects.filter(Q(phone__contains=search_phone) | Q(realname__contains=search_realname))
    print("这是guest_list-------------------------------")
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
    # print(guest_list)
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


# 项目管理
@login_required
def project_manage(request):
    project_list = ProjectInfo.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    return render(request, "project_manage.html", {"user": username, "projects": project_list})


# 项目搜索
@login_required
def search_project(request):
    username = request.session.get('user', '')
    search_project = request.GET.get("project_name", "")
    print(username)
    print(search_project)
    project_list = ProjectInfo.objects.filter(project_name__contains=search_project)
    # 修改project_name__contains，为搜索字段的名字
    print(project_list)
    return render(request, "project_manage.html", {"user": username, "projects": project_list})


# 接口管理
@login_required
def interface_manage(request):
    interface_list = InterfaceInfo.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    paginator = Paginator(interface_list, 10)                                                    # 创建每页5条数据的分页器
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "interface_manage.html", {"user": username, "interfaces": contacts})


# 接口查询
@login_required
def search_interface(request):
    username = request.session.get('user', '')
    search_interface = request.GET.get("interface_name", "")
    interface_list = InterfaceInfo.objects.filter(interface_name__contains=search_interface)
    paginator = Paginator(interface_list, 10)                                                    # 创建每页5条数据的分页器
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "interface_manage.html", {"user": username, "interfaces": contacts})


# 字段管理
@login_required
def field_manage(request):
    field_list = InterfaceField.objects.all()
    # username = request.COOKIES.get('user', '')  # 读取浏览器cookie
    username = request.session.get('user', '')  # 读取浏览器session
    paginator = Paginator(field_list, 10)                                                    # 创建每页5条数据的分页器
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "field_manage.html", {"user": username, "fields": contacts})


# 字段查询
@login_required
def search_field(request):
    username = request.session.get('user', '')
    search_filed = request.GET.get("filed_name", "")
    field_list = InterfaceInfo.objects.filter(filed_name__contains=search_field)
    paginator = Paginator(field_list, 10)                                                    # 创建每页5条数据的分页器
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页面数据
        contacts = paginator.page(paginator.num_pages)
    return render(request, "field_manage.html", {"user": username, "fields": contacts})
