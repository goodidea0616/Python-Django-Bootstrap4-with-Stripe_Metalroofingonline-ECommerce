# Generated by Django 2.0.5 on 2019-02-10 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_auto_20181031_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='date_delivered',
            field=models.DateField(blank=True, null=True),
        ),
    ]