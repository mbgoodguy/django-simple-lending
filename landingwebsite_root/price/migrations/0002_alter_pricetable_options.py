# Generated by Django 4.2 on 2023-05-10 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricetable',
            options={'verbose_name': 'Услуги', 'verbose_name_plural': 'Услуги'},
        ),
    ]