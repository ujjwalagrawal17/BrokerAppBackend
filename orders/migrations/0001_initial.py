# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-01 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(blank=True, max_length=20, null=True)),
                ('buyer_id', models.CharField(blank=True, max_length=20, null=True)),
                ('seller_id', models.CharField(blank=True, max_length=20, null=True)),
                ('product_id', models.IntegerField(default=0)),
                ('product_name', models.CharField(blank=True, max_length=56, null=True)),
                ('product_quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('buying_price', models.IntegerField(default=0)),
                ('selling_price', models.IntegerField(default=0)),
                ('truck_number', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=512, null=True)),
                ('show', models.BooleanField(default=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
