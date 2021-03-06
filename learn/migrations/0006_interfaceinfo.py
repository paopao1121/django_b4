# Generated by Django 2.1.9 on 2019-06-18 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0005_auto_20190618_1955'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterfaceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interface_code', models.CharField(max_length=10, verbose_name='接口编码')),
                ('interface_name', models.CharField(max_length=100, verbose_name='接口名称')),
                ('interface_type', models.CharField(max_length=100, verbose_name='接口类型')),
                ('request_type', models.CharField(max_length=10, verbose_name='请求方式')),
                ('byref_type', models.CharField(max_length=10, verbose_name='传参方式')),
                ('request_url', models.CharField(max_length=300, verbose_name='请求URL')),
                ('headers_label_one', models.CharField(max_length=50, verbose_name='请求报文头标签1')),
                ('headers_content_one', models.CharField(max_length=1000, verbose_name='请求报文头内容1')),
                ('headers_label_two', models.CharField(max_length=50, verbose_name='请求报文头标签2')),
                ('headers_content_two', models.CharField(max_length=1000, verbose_name='请求报文头内容2')),
                ('request_json', models.CharField(max_length=4000, verbose_name='请求报文模板')),
                ('response_json', models.CharField(max_length=4000, verbose_name='响应报文模板')),
                ('remarks', models.CharField(max_length=2000, verbose_name='备注')),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('validate_state', models.BooleanField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.ProjectInfo')),
            ],
        ),
    ]
