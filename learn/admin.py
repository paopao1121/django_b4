from django.contrib import admin
from learn.models import Event, Guest, ProjectInfo, InterfaceInfo, InterfaceField
from learn.models import PublicRule, PublicCase, BatchJob, BatchCase
from learn.models import AppServer

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
    list_display = ['project_name', 'parent_id', 'project_type', 'create_time']
    search_fields = ['project_name']
    list_filter = ['validate_state']


class InterfaceInfoAdmin(admin.ModelAdmin):
    list_display = ['project', 'interface_code', 'interface_name', 'interface_type', 'request_type', 'byref_type',
                    'request_url', 'remarks', 'create_time']
    search_fields = ['interface_code', 'interface_name', 'project']
    list_filter = ['validate_state']


class InterfaceFieldAdmin(admin.ModelAdmin):
    list_display = ['interface', 'field_value', 'field_name', 'type', 'length', 'belong_list',
                    'belong_dict', 'dependent_field', 'dependent_value', 'is_null', 'default_value']
    search_fields = ['interface_code', 'field_value', 'field_name', 'interface']
    list_filter = ['validate_state']


class PublicRuleAdmin(admin.ModelAdmin):
    list_display = ['rules_name', 'rules_type', 'data_format', 'rule_comment',
                    'remarks', 'create_time']
    search_fields = ['rules_name', 'rules_type', 'data_format']
    list_filter = ['validate_state']


class PublicCaseAdmin(admin.ModelAdmin):
    list_display = ['case_name', 'field_id', 'rule_id', 'version', 'create_time']
    search_fields = ['case_name', 'field_id', 'rule_id']
    list_filter = ['validate_state']


class BatchJobAdmin(admin.ModelAdmin):
    list_display = ['id', 'batch_status', 'start_time', 'finish_time', 'execute_frequency', 'create_time']
    search_fields = ['case_name', 'field_id', 'rule_id']
    list_filter = ['validate_state']


class BatchCaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'case_status', 'public_case_id', 'job_id', 'request_json', 'response_json', 'create_time']
    search_fields = ['id', 'case_status', 'public_case_id', 'job_id']
    list_filter = ['validate_state']


class AppServerAdmin(admin.ModelAdmin):
    list_display = ['id', 'server_name', 'server_ip', 'server_port', 'create_time']
    search_fields = ['server_name']
    list_filter = ['validate_state']


admin.site.register(Event, EventAdmin)      # 需要注册EventAdmin, GuestAdmin才能显示多栏位
admin.site.register(Guest, GuestAdmin)
admin.site.register(ProjectInfo, ProjectInfoAdmin)                  # 注册项目信息ProjectInfoAdmin，才可以直接在后台进行管理
admin.site.register(InterfaceInfo, InterfaceInfoAdmin)              # 注册接口信息InterfaceInfoAdmin，才可以直接在后台进行管理
admin.site.register(InterfaceField, InterfaceFieldAdmin)            # 注册接口字段信息InterfaceField，才可以直接在后台进行管理
admin.site.register(PublicRule, PublicRuleAdmin)                    # 注册公共规则PublicRule，才可以直接在后台进行管理
admin.site.register(PublicCase, PublicCaseAdmin)                    # 注册公共规则PublicCase，才可以直接在后台进行管理
admin.site.register(BatchJob, BatchJobAdmin)                        # 注册批次任务PublicCase，才可以直接在后台进行管理
admin.site.register(BatchCase, BatchCaseAdmin)                        # 注册批次用例BatchCase，才可以直接在后台进行管理
admin.site.register(AppServer, AppServerAdmin)                        # 注册批次用例BatchCase，才可以直接在后台进行管理
