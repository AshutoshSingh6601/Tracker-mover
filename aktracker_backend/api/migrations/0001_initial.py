# Generated by Django 4.2.9 on 2024-02-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('moveFrom', models.CharField(max_length=100)),
                ('moveTo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('rantal', models.CharField(max_length=100)),
                ('seeUs', models.CharField(max_length=100)),
            ],
        ),
    ]
