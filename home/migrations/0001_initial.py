# Generated by Django 4.0.4 on 2022-05-31 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='faculties/')),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2022, 6, 1, 3, 4, 7, 688887))),
                ('date_of_joining', models.DateField(blank=True, default=datetime.datetime(2022, 6, 1, 3, 4, 7, 688887))),
                ('email', models.EmailField(default='email', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=30)),
                ('branch', models.CharField(choices=[('E & C', 'E & C'), ('MECHANICAL', 'MECHANICAL'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE')], max_length=30)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('usn', models.AutoField(primary_key=True, serialize=False)),
                ('student_usn', models.CharField(max_length=30, unique=True)),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('date_of_birth', models.DateField(blank=True, default=datetime.datetime(2022, 6, 1, 3, 4, 7, 689912))),
                ('date_of_joining', models.DateField(blank=True, default=datetime.datetime(2022, 6, 1, 3, 4, 7, 689912))),
                ('email', models.EmailField(default='email', max_length=30)),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], default='MALE', max_length=10)),
                ('branch', models.CharField(choices=[('E & C', 'E & C'), ('MECHANICAL', 'MECHANICAL'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE')], max_length=30)),
                ('division', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30)),
                ('sem', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])),
                ('created_date', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='StudentAttendences',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('student_usn', models.CharField(max_length=30, unique=True)),
                ('status', models.BooleanField()),
                ('branch', models.CharField(choices=[('E & C', 'E & C'), ('MECHANICAL', 'MECHANICAL'), ('COMPUTER SCIENCE', 'COMPUTER SCIENCE')], max_length=30)),
                ('division', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=30)),
                ('subject', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=30)),
                ('sem', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_name', models.CharField(default='add first name', max_length=30)),
                ('sem', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)])),
            ],
        ),
    ]
