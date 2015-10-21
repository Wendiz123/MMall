# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20151019_0637'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to=b'', blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(default=0, max_digits=1, decimal_places=1),
        ),
    ]
