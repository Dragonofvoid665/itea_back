# Generated by Django 5.1.4 on 2025-06-21 09:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images')),
                ('price', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tm', models.CharField(max_length=255)),
                ('title_ru', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='static/images/')),
                ('content_tm', models.TextField()),
                ('content_ru', models.TextField()),
                ('content_en', models.TextField()),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('places', models.PositiveBigIntegerField(default=0)),
                ('ordered_places', models.PositiveBigIntegerField(default=0)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=200)),
                ('name_ru', models.CharField(max_length=200)),
                ('name_tm', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='static/images')),
                ('role', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vacansy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('title_en', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('title_tm', models.CharField(max_length=255, verbose_name='Название вакансии')),
                ('image', models.ImageField(upload_to='static/images')),
                ('description_en', models.CharField(max_length=200)),
                ('description_ru', models.CharField(max_length=200)),
                ('description_tm', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=150)),
                ('phone_number', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=200)),
                ('name_ru', models.CharField(max_length=200)),
                ('name_tm', models.CharField(max_length=200)),
                ('description_en', models.CharField(max_length=200)),
                ('description_ru', models.CharField(max_length=200)),
                ('description_tm', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('duration', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_iteea.course_category')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
    ]
