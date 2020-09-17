# Generated by Django 3.1.1 on 2020-09-17 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mileage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('insurance', models.CharField(choices=[('special', 'Special'), ('standard', 'Standard'), ('light', 'Light'), ('none', 'None')], default='none', max_length=40)),
                ('from_when', models.DateTimeField()),
                ('to_when', models.DateTimeField()),
                ('rental_date', models.DateTimeField(auto_now=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='cars.car')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('payment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='reservations.payment')),
            ],
        ),
    ]
