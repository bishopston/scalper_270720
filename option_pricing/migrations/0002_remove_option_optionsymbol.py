# Generated by Django 3.0.8 on 2020-07-27 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='optionsymbol',
        ),
    ]
