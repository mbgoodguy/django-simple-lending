# Generated by Django 4.2 on 2023-05-15 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_cmsslider_cms_css_alter_cmsslider_cms_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsslider',
            name='cms_img',
            field=models.ImageField(upload_to='sliderimg/', verbose_name='Изображение'),
        ),
    ]
