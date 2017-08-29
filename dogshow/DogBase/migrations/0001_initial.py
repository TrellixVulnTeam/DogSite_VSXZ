# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dogName', models.CharField(max_length=400)),
                ('dogShortName', models.CharField(max_length=200)),
                ('dogBday', models.DateField()),
                ('dogDef', models.TextField()),
                ('dogPath', models.CharField(max_length=200)),
                ('dogSex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('dogIsPuppy', models.BooleanField()),
                ('dogIsOurs', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeDog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='dog',
            name='dogType',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DogBase.TypeDog'),
        ),
    ]