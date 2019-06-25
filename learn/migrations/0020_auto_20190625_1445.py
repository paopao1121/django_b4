# Generated by Django 2.1.9 on 2019-06-25 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0019_auto_20190625_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appserver',
            options={'verbose_name': '应用服务器', 'verbose_name_plural': '应用服务器管理'},
        ),
        migrations.AlterModelOptions(
            name='batchcase',
            options={'verbose_name': '批次用例', 'verbose_name_plural': '批次用例管理'},
        ),
        migrations.AlterModelOptions(
            name='batchjob',
            options={'verbose_name': '批次任务', 'verbose_name_plural': '批次任务管理'},
        ),
        migrations.AlterModelOptions(
            name='interfacefield',
            options={'verbose_name': '接口字段', 'verbose_name_plural': '接口字段管理'},
        ),
        migrations.AlterModelOptions(
            name='interfaceinfo',
            options={'verbose_name': '接口', 'verbose_name_plural': '接口管理'},
        ),
        migrations.AlterModelOptions(
            name='projectinfo',
            options={'verbose_name': '项目', 'verbose_name_plural': '项目管理'},
        ),
        migrations.AlterModelOptions(
            name='publiccase',
            options={'verbose_name': '公共用例', 'verbose_name_plural': '公共用例管理'},
        ),
        migrations.AlterModelOptions(
            name='publicrule',
            options={'verbose_name': '公共规则', 'verbose_name_plural': '公共规则管理'},
        ),
    ]
