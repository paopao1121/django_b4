"""django_b4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from learn import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login_action/', views.login_action),
    path('event_manage/', views.event_manege),
    path('', views.index),                                          # 效果一样
    path('index/', views.index),                                    # 效果一样
    path('accounts/login/', views.index),                           # 效果一样
    path('search_name/', views.search_name),                        # 搜索
    path('guest_manage/', views.guest_manage),                      # 搜索发布会
    path('search_guest/', views.search_guest),                      # 搜索嘉宾
    # url(r'^sign_index/(?P<eid>[0-9]+)/$', views.sign_index),         # 签到
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),      # 签到
    path('logout/', views.logout),                      # 退出
]
