# Generated by Django 3.1.3 on 2020-11-29 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_ordermodel_is_shipped'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='state',
        ),
    ]
