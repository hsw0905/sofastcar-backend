# Generated by Django 3.1.1 on 2020-09-23 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_price', models.PositiveIntegerField(default=0)),
                ('min_price_per_km', models.PositiveIntegerField(default=0)),
                ('mid_price_per_km', models.PositiveIntegerField(default=0)),
                ('max_price_per_km', models.PositiveIntegerField(default=0)),
                ('car', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='carprice', to='cars.car')),
            ],
        ),
    ]
