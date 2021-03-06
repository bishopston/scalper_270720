# Generated by Django 3.0.8 on 2020-08-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0007_auto_20200819_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionsymbol', models.CharField(default='_', max_length=15)),
                ('date', models.DateTimeField()),
                ('asset', models.CharField(max_length=10)),
                ('optiontype', models.CharField(max_length=4)),
                ('expmonthyear', models.DateField()),
                ('closing_price', models.FloatField()),
                ('change', models.FloatField()),
                ('volume', models.IntegerField()),
                ('max', models.FloatField()),
                ('min', models.FloatField()),
                ('trades', models.IntegerField()),
                ('fixing_price', models.FloatField()),
                ('open_interest', models.IntegerField()),
            ],
        ),
    ]
