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
    path('index/', views.index),                                                    # 效果一样
    path('login_action/', views.login_action),                                      # 登录动作
    path('logout/', views.logout),                                                  # 退出
    url(r'^sign_index_action/(?P<eid>[0-9]+)/$', views.sign_index_action),          # 签到

    path('event_manage/', views.event_manege),                                      # 发布会管理
    path('search_name/', views.search_name),                                        # 发布会搜索

    path('guest_manage/', views.guest_manage),                                      # 嘉宾管理
    path('search_guest/', views.search_guest),                                      # 搜索嘉宾

    path('project_manage/', views.project_manage),                                  # 项目管理
    path('search_project/', views.search_project),                                  # 项目搜索

    path('interface_manage/', views.interface_manage),                              # 接口管理
    path('search_interface/', views.search_interface),                              # 接口搜索

    path('field_manage/', views.field_manage),                                      # 接口字段管理
    path('search_field/', views.search_field),                                      # 接口字段搜索

    path('public_rule/', views.public_rule),                                        # 公共规则管理
    path('search_rule/', views.search_rule),                                        # 公共规则搜索

    path('public_case/', views.public_case),                                        # 公共用例管理
    path('search_public_case/', views.search_public_case),                          # 公共用例搜索

    path('batch_job/', views.batch_job),                                            # 批次任务管理
    path('search_job/', views.search_job),                                          # 批次任务搜索

    path('batch_case/', views.batch_case),                                          # 批次任务管理
    path('search_case/', views.search_case),                                        # 批次任务搜索
]
