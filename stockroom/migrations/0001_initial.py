# Generated by Django 2.2.6 on 2020-02-01 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('product_info', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('date', models.DateField()),
                ('price', models.IntegerField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockroom.Person')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stockroom.Product')),
            ],
        ),
    ]
