# Generated by Django 2.1.9 on 2019-06-25 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0014_appserver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appserver',
            name='server_ip',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='服务器IP'),
        ),
    ]
