from django.db import models


# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(max_length=200, verbose_name='Заголовок')
    cms_text = models.CharField(max_length=200, verbose_name='Заголовок')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
