from django.db import models
import datetime

# Create your models here.
from core.utils import time_format


class CarPrice(models.Model):
    car = models.OneToOneField('cars.Car', related_name='carprice', on_delete=models.CASCADE)
    standard_price = models.PositiveIntegerField(default=0)

    # 주행거리 구간별 이용 요금, 많이 달릴수록 할인 (0~30km : max , 31~100km : mid, 101km~: min)
    min_price_per_km = models.PositiveIntegerField(default=0)
    mid_price_per_km = models.PositiveIntegerField(default=0)
    max_price_per_km = models.PositiveIntegerField(default=0)

    # 주중 : 월 ~ 목, KST
    # 주말 : 금 ~ 일, KST
    # 주중 / 주말 10분당 요금 (차량 급에 따라 달라짐)
    weekday_price_per_ten_min = models.PositiveIntegerField(default=0)
    weekend_price_per_ten_min = models.PositiveIntegerField(default=0)

    def str_to_date_time_UTC(self, str_date_time):
        return time_format(str_date_time)

    def get_price(self, date_time_start, date_time_end):
        date_time_start = self.str_to_date_time_UTC(date_time_start)
        date_time_end = self.str_to_date_time_UTC(date_time_end)
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.standard_price + count_ten_minutes * self.weekday_price_per_ten_min)
        return rental_price

    def get_price_from_iso_format(self, date_time_start, date_time_end):
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.standard_price + count_ten_minutes * self.weekday_price_per_ten_min)
        return rental_price


# 차량손해면책 상품
class InsuranceFee(models.Model):
    car = models.OneToOneField('cars.Car', related_name='insurances', on_delete=models.CASCADE)

    # 차량 급에 따라 기본 보험료(30분기준)가 달라짐
    light_price = models.PositiveIntegerField(default=0)
    standard_price = models.PositiveIntegerField(default=0)
    special_price = models.PositiveIntegerField(default=0)

    # 차량 급에 따라 10분당 증가되는 가격
    light_price_per_ten_min = models.PositiveIntegerField(default=0)
    standard_price_per_ten_min = models.PositiveIntegerField(default=0)
    special_price_per_ten_min = models.PositiveIntegerField(default=0)

    def str_to_date_time_UTC(self, str_date_time):
        return time_format(str_date_time)

    def get_light_price(self, date_time_start, date_time_end):
        date_time_start = self.str_to_date_time_UTC(date_time_start)
        date_time_end = self.str_to_date_time_UTC(date_time_end)
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.light_price + count_ten_minutes * self.light_price_per_ten_min)
        return rental_price

    def get_light_price_from_iso_format(self, date_time_start, date_time_end):
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.light_price + count_ten_minutes * self.light_price_per_ten_min)
        return rental_price

    def get_standard_price(self, date_time_start, date_time_end):
        date_time_start = self.str_to_date_time_UTC(date_time_start)
        date_time_end = self.str_to_date_time_UTC(date_time_end)
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.standard_price + count_ten_minutes * self.standard_price_per_ten_min)
        return rental_price

    def get_standard_price_from_iso_format(self, date_time_start, date_time_end):
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.standard_price + count_ten_minutes * self.standard_price_per_ten_min)
        return rental_price

    def get_special_price(self, date_time_start, date_time_end):
        date_time_start = self.str_to_date_time_UTC(date_time_start)
        date_time_end = self.str_to_date_time_UTC(date_time_end)
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.special_price + count_ten_minutes * self.special_price_per_ten_min)
        return rental_price

    def get_special_price_from_iso_format(self, date_time_start, date_time_end):
        total_minutes = (date_time_end - date_time_start).total_seconds() / 60
        count_ten_minutes = (total_minutes - 30) / 10
        rental_price = int(self.special_price + count_ten_minutes * self.special_price_per_ten_min)
        return rental_price

class Coupon(models.Model):
    member = models.ForeignKey('members.Member', related_name='coupons', on_delete=models.CASCADE)
    date_time_start = models.DateTimeField(auto_created=True, help_text='쿠폰사용시작시간')
    expire_date_time = models.DateTimeField(help_text='만료시간')
    title = models.CharField(max_length=100, help_text='쿠폰명')
    limit_delta_term = models.PositiveIntegerField(default=0, help_text='N일이상 예약 제한 체크용')
    discount_fee = models.PositiveIntegerField(default=0, help_text='할인금액')
    is_enabled = models.BooleanField(default=True, help_text='사용가능여부')
    will_use_check = models.BooleanField(default=False, help_text='사용시체크')
    is_used = models.BooleanField(default=False, help_text='사용했는지여부')
    is_free = models.BooleanField(default=False, help_text='무료쿠폰여부')
    description = models.CharField(max_length=160, null=True, help_text='부가설명')
    created_at = models.DateTimeField(auto_now_add=True, help_text='TimeStamp')
    updated_at = models.DateTimeField(auto_now=True)