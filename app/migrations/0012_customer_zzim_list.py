# Generated by Django 3.1.2 on 2020-10-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20201021_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='zzim_list',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
