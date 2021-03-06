# Generated by Django 3.2.8 on 2021-10-20 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=60, verbose_name='产品名称')),
                ('belong', models.CharField(max_length=60, verbose_name='券商')),
                ('type', models.CharField(max_length=60, verbose_name='账户类型')),
                ('account', models.CharField(max_length=60, verbose_name='账户号')),
                ('card_sh', models.CharField(max_length=60, verbose_name='上海卡号')),
                ('card_sz', models.CharField(max_length=60, verbose_name='深圳卡号')),
                ('start_date', models.DateField(verbose_name='账户启用日期')),
                ('end_date', models.DateField(verbose_name='账户销户日期')),
                ('business_department', models.CharField(max_length=120, verbose_name='所属营业部')),
                ('contacts', models.CharField(max_length=60, verbose_name='联系人')),
                ('contact_email', models.CharField(max_length=60, verbose_name='联系邮箱')),
                ('contact_mob', models.CharField(max_length=60, verbose_name='联系手机')),
                ('contact_tel', models.CharField(max_length=60, verbose_name='联系电话')),
                ('contact_weixin', models.CharField(max_length=60, verbose_name='联系微信')),
                ('status', models.CharField(max_length=60)),
                ('trader', models.CharField(max_length=60, verbose_name='认领交易员')),
                ('salesman', models.CharField(max_length=60, verbose_name='认领销售员')),
                ('backstage_staff', models.CharField(max_length=60, verbose_name='认领后台员')),
                ('notes', models.CharField(max_length=255, verbose_name='')),
            ],
        ),
    ]
