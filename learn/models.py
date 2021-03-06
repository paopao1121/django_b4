from django.db import models

# Create your models here.
# 发布会表


class Event(models.Model):
    name = models.CharField(max_length=100)                             # 发布会标题
    limit = models.IntegerField()                                       # 参加人数
    status = models.BooleanField()                                      # 状态
    address = models.CharField(max_length=200)                          # 地址
    start_time = models.DateTimeField('event_time')                     # 发布会时间
    create_time = models.DateTimeField(auto_now=True)                   # 创建时间，自动获取当前时间

    def __str__(self):
        return self.name
        # return (self.id, self.name, self.status, self.address, self.start_time)


# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)          # 关联发布会 id  在外键值的后面加上 on_delete=models.CASCADE
    realname = models.CharField(max_length=64)                          # 姓名
    phone = models.CharField(max_length=16)                             # 手机
    email = models.EmailField()                                         # 邮箱
    sign = models.BooleanField()                                        # 签到状态
    create_time = models.DateTimeField(auto_now=True)                   # 创建时间，自动获取当前时间

    class Meta:
        unique_together = ("event", "phone")

    def __str__(self):
        return self.realname


# 项目信息表
class ProjectInfo(models.Model):
    # id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100, verbose_name='项目名称')
    parent_id = models.CharField(max_length=4, verbose_name='归属条线')
    project_type = models.CharField(max_length=4, verbose_name='项目类型')  # 项目类型(1：WEB，2：APP)
    create_time = models.DateTimeField(auto_now=True)                   # 创建时间，自动获取当前时间
    validate_state = models.BooleanField()   # 数据有效性(1：有效，0：无效)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = '项目'               # 点击verbose_name_plural进入详情页后，显示的标题
        verbose_name_plural = '项目管理'    # admin页app下列表展示


# 接口信息表
class InterfaceInfo(models.Model):
    project = models.ForeignKey(ProjectInfo, on_delete=models.CASCADE)
    interface_code = models.CharField(max_length=10, verbose_name='接口编码')
    interface_name = models.CharField(max_length=100, verbose_name='接口名称')
    interface_type = models.CharField(max_length=100, verbose_name='接口类型')  # 接口类型(1：WEB，2：APP)
    request_type = models.CharField(max_length=10, verbose_name='请求方式')     # 请求方式(1：POST，2：GET)
    byref_type = models.CharField(max_length=10, verbose_name='传参方式')       # 传参方式(1：json)
    request_url = models.CharField(max_length=300, verbose_name='请求URL')
    headers_label_one = models.CharField(max_length=50, verbose_name='请求报文头标签1')
    headers_content_one = models.CharField(max_length=1000, verbose_name='请求报文头内容1')
    headers_label_two = models.CharField(max_length=50, verbose_name='请求报文头标签2', blank=True)
    headers_content_two = models.CharField(max_length=1000, verbose_name='请求报文头内容2', blank=True)
    request_json = models.TextField(verbose_name='请求报文模板', blank=True)
    response_json = models.TextField(verbose_name='响应报文模板', blank=True)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True)
    create_time = models.DateTimeField(auto_now=True)                           # 创建时间，自动获取当前时间
    validate_state = models.BooleanField(verbose_name='是否有效')               # 数据有效性(1：有效，0：无效)

    def __str__(self):
        return self.interface_code

    class Meta:
        verbose_name = '接口'
        verbose_name_plural = '接口管理'


# 接口字段表
class InterfaceField(models.Model):
    interface = models.ForeignKey(InterfaceInfo, on_delete=models.CASCADE)
    field_value = models.CharField(max_length=100, verbose_name='接口字段')
    field_name = models.CharField(max_length=100, verbose_name='接口名称')
    # 字段数据类型(1：VARCHAR，2：INT，3：LIST，4：DATE，5：DATETIME，6：FLOAT)
    type = models.CharField(max_length=100, verbose_name='数据类型')
    length = models.IntegerField(verbose_name='字段长度', blank=True)   # blank=True 字段可为空，=False 字段不可为空
    belong_list = models.CharField(max_length=40, verbose_name='归属LIST', blank=True)
    belong_dict = models.CharField(max_length=40, verbose_name='归属DICT', blank=True)
    dependent_field = models.CharField(max_length=40, verbose_name='依赖字段', blank=True)
    dependent_value = models.CharField(max_length=40, verbose_name='依赖值', blank=True)
    is_null = models.BooleanField(verbose_name='是否可空')
    default_value = models.CharField(max_length=100, verbose_name='默认值', blank=True)
    remarks = models.CharField(max_length=2000, verbose_name='备注', blank=True)
    validate_state = models.BooleanField(verbose_name='是否有效')               # 数据有效性(1：有效，0：无效)
    create_time = models.DateTimeField(auto_now=True)                           # 创建时间，自动获取当前时间

    def __str__(self):
        return self.field_value

    class Meta:
        verbose_name = '接口字段'
        verbose_name_plural = '接口字段管理'


# 公共规则表
class PublicRule(models.Model):
    rules_name = models.CharField(max_length=40, verbose_name='规则名称')
    rules_type = models.CharField(max_length=10, verbose_name='规则类型')  # 规则类型(1：数据类型规则，2：基础校验规则)
    data_format = models.CharField(max_length=40, verbose_name='数据格式')
    rule_comment = models.CharField(max_length=100, verbose_name='规则描述', blank=True)
    regexp_1 = models.CharField(max_length=100, verbose_name='正则表达式1', blank=True)
    regexp_2 = models.CharField(max_length=100, verbose_name='正则表达式2', blank=True)
    regexp_3 = models.CharField(max_length=100, verbose_name='正则表达式3', blank=True)
    regexp_4 = models.CharField(max_length=100, verbose_name='正则表达式4', blank=True)
    regexp_5 = models.CharField(max_length=100, verbose_name='正则表达式5', blank=True)
    regexp_6 = models.CharField(max_length=100, verbose_name='正则表达式6', blank=True)
    regexp_7 = models.CharField(max_length=100, verbose_name='正则表达式7', blank=True)
    regexp_8 = models.CharField(max_length=100, verbose_name='正则表达式8', blank=True)
    regexp_9 = models.CharField(max_length=100, verbose_name='正则表达式9', blank=True)
    regexp_10 = models.CharField(max_length=100, verbose_name='正则表达式10', blank=True)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True)
    validate_state = models.BooleanField(verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.rules_name

    class Meta:
        verbose_name = '公共规则'
        verbose_name_plural = '公共规则管理'


# 公共用例表
class PublicCase(models.Model):
    field_id = models.ForeignKey(InterfaceField, on_delete=models.CASCADE)
    rule_id = models.ForeignKey(PublicRule, on_delete=models.CASCADE)
    case_name = models.CharField(max_length=100, verbose_name='用例名称', blank=True)
    request_json = models.TextField(verbose_name='请求报文模板', blank=True)
    response_json = models.TextField(verbose_name='响应报文模板', blank=True)
    version = models.CharField(max_length=10, verbose_name='用例版本号', blank=True)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True)
    validate_state = models.BooleanField(verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_name

    class Meta:
        verbose_name = '公共用例'
        verbose_name_plural = '公共用例管理'


# 批次任务表
class BatchJob(models.Model):
    batch_status = models.CharField(max_length=2, verbose_name='批次状态', blank=True)
    # 批次状态(0：初始录入，1：执行中，2：执行完成，3：执行失败)
    start_time = models.DateTimeField(auto_now_add=True, verbose_name='执行开始时间')    # auto_now_add
    finish_time = models.DateTimeField(verbose_name='执行结束时间')
    execute_frequency = models.IntegerField(verbose_name='执行次数')
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True)
    validate_state = models.BooleanField(verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '批次任务'
        verbose_name_plural = '批次任务管理'


# 批次用例表
class BatchCase(models.Model):
    public_case_id = models.ForeignKey(PublicCase, on_delete=models.CASCADE)
    job_id = models.ForeignKey(BatchJob, on_delete=models.CASCADE)
    case_status = models.CharField(max_length=2, verbose_name='用例状态', blank=True)
    # 用例状态(0：初始录入，1：执行中，2：成功，3：失败，4：人工判定)
    request_json = models.TextField(verbose_name='请求报文', blank=True)
    response_json = models.TextField(verbose_name='响应报文', blank=True)
    remarks = models.CharField(max_length=200, verbose_name='备注', blank=True)
    validate_state = models.BooleanField(verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = '批次用例'
        verbose_name_plural = '批次用例管理'


# 应用服务器信息表
class AppServer(models.Model):
    server_name = models.CharField(max_length=64, verbose_name='服务器名称', blank=True, null=True)
    server_ip = models.CharField(max_length=64, verbose_name='服务器IP', blank=True, null=True)
    server_port = models.CharField(max_length=6, verbose_name='服务器端口', blank=True, null=True)
    validate_state = models.BooleanField(verbose_name='是否有效')
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.server_name

    class Meta:
        verbose_name = '应用服务器'
        verbose_name_plural = '应用服务器管理'
