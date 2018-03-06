# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-06 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Corpus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transcript', models.TextField()),
                ('corpus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speech_captcha.Corpus')),
            ],
        ),
        migrations.CreateModel(
            name='Utterance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utterance', models.FileField(upload_to=b'')),
                ('transcript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='speech_captcha.Sentence')),
            ],
        ),
    ]