# Generated by Django 2.0.3 on 2018-05-01 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20180501_0942'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalDropDown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdditionalDropDown', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='AdditionalDropDownOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Image')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
    ]