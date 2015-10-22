# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0010_cart_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='member',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='total',
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='customer_name',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=0),
        ),
    ]
