# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_remove_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, max_digits=10, decimal_places=0),
        ),
    ]
