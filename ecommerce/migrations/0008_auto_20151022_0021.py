# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_auto_20151019_0703'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('qty', models.IntegerField(default=0)),
                ('total', models.DecimalField(default=0, max_digits=10, decimal_places=0)),
            ],
        ),
        migrations.DeleteModel(
            name='CarItem',
        ),
        migrations.AddField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cart',
            name='date_transaction',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(to='ecommerce.Cart'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(to='ecommerce.Product'),
        ),
    ]
