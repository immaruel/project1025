# Generated by Django 3.0.7 on 2020-10-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20201021_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='save',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='cart',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='like',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='packing',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='price',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='sales',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='set',
            name='save',
            field=models.IntegerField(null=True),
        ),
    ]
