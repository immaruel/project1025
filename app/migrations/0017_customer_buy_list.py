# Generated by Django 2.2.1 on 2020-10-25 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_delete_set'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='buy_list',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
