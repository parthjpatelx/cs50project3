# Generated by Django 2.0.3 on 2020-06-15 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200615_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='toppings_int',
            new_name='toppings',
        ),
    ]