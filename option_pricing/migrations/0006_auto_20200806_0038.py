# Generated by Django 3.0.8 on 2020-08-05 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('option_pricing', '0005_auto_20200806_0037'),
    ]

    operations = [
        migrations.CreateModel(
            name='OptionAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='optionsymbol',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
