# Generated by Django 3.1.1 on 2020-10-03 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('reservations', '0002_auto_20201001_2031'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TollFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toll_gate', models.CharField(max_length=30)),
                ('toll_fee', models.PositiveIntegerField(help_text='통행료')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TimeStamp')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toll_fees', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toll_fees', to='reservations.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBeforeUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_fee', models.PositiveIntegerField(help_text='운행전대여료')),
                ('insurance_fee', models.PositiveIntegerField(help_text='차량손해면책보험료')),
                ('coupon_discount', models.PositiveIntegerField(default=0, help_text='쿠폰할인가격')),
                ('etc_discount', models.PositiveIntegerField(default=0, help_text='기타할인금액')),
                ('extension_fee', models.PositiveIntegerField(default=0, help_text='연장요금')),
                ('total_fee', models.PositiveIntegerField(help_text='총운행전요금')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TimeStamp')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_before', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_before', to='reservations.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentAfterUse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driving_distance', models.PositiveIntegerField(help_text='운행거리')),
                ('first_section_fee', models.PositiveIntegerField(help_text='0~30km 구간 주행요금')),
                ('second_section_fee', models.PositiveIntegerField(help_text='31~100km 구간 주행요금')),
                ('third_section_fee', models.PositiveIntegerField(help_text='100km 이후 주행요금')),
                ('total_toll_fee', models.PositiveIntegerField(default=0, help_text='총통행료')),
                ('total_fee', models.PositiveIntegerField(help_text='총운행후요금')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TimeStamp')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_after', to=settings.AUTH_USER_MODEL)),
                ('reservation', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='payment_after', to='reservations.reservation')),
            ],
        ),
    ]
