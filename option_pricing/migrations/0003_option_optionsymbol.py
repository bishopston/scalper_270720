# Generated by Django 3.0.8 on 2020-07-27 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0002_remove_option_optionsymbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='option',
            name='optionsymbol',
            field=models.CharField(default='_', max_length=15),
        ),
    ]
