# Generated by Django 3.1.1 on 2020-09-24 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200924_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingorder',
            name='zipcode',
            field=models.IntegerField(null=True),
        ),
    ]
