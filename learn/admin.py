from django.contrib import admin
from learn.models import Event, Guest, ProjectInfo, InterfaceInfo, InterfaceField

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']        # 表格表头
    search_fields = ['name']    # 搜索栏
    list_filter = ['status']    # 过滤器


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']    # 搜索栏
    list_filter = ['sign']    # 过滤器


class ProjectInfoAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'parent_id', 'project_type', 'create_time', 'validate_state']
    search_fields = ['project_name']
    list_filter = ['validate_state']


class InterfaceInfoAdmin(admin.ModelAdmin):
    list_display = ['project', 'interface_code', 'interface_name', 'interface_type', 'request_type', 'byref_type',
                    'request_url', 'remarks', 'create_time', 'validate_state']
    search_fields = ['interface_code', 'interface_name', 'project']
    list_filter = ['validate_state']


class InterfaceFieldAdmin(admin.ModelAdmin):
    list_display = ['interface', 'field_value', 'field_name', 'type', 'length', 'belong_list',
                    'belong_dict', 'dependent_field', 'dependent_value', 'is_null', 'default_value',
                    'remarks', 'create_time', 'validate_state']
    search_fields = ['interface_code', 'field_value', 'field_name', 'interface']
    list_filter = ['validate_state']


admin.site.register(Event, EventAdmin)      # 需要注册EventAdmin, GuestAdmin才能显示多栏位
admin.site.register(Guest, GuestAdmin)
admin.site.register(ProjectInfo, ProjectInfoAdmin)
admin.site.register(InterfaceInfo, InterfaceInfoAdmin)
admin.site.register(InterfaceField, InterfaceFieldAdmin)

