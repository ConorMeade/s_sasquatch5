# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-12-03 22:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodpost',
            name='roomNum',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='location',
            field=models.CharField(choices=[('library', 'W.E.B. Du Bois Library'), ('hamp', 'Hampshire Dining Hall'), ('berk', 'Berkshire Dining Hall'), ('woo', 'Worcester Dining Hall'), ('frank', 'Franklin Dining Hall'), ('l', 'Lederle Tower'), ('Sc', 'South College'), ('rec', 'Campus Rec Center'), ('cs', 'Computer Science Building'), ('Thom', 'Thompson'), ('mor', 'Morrill 3')], max_length=100),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='postInfo',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='foodpost',
            name='postScore',
            field=models.IntegerField(default=0),
        ),
    ]
