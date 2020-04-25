# Generated by Django 3.0.4 on 2020-04-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='order_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]