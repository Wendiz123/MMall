# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0008_auto_20151022_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
