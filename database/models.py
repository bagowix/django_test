from django.db import models


class DataBase(models.Model):
    CHOICES_UNIT = [
        ('Штук', 'Штук'),
        ('Килограмм', 'Килограмм'),
        ('Литров', 'Литров')
    ]
    productName = models.CharField('Название товара', max_length=250)
    quantity = models.PositiveIntegerField('Количество товара')
    unit = models.CharField('Единица измерения', choices=CHOICES_UNIT, max_length=10)
    price = models.PositiveIntegerField('Цена товара')
    date = models.DateField('Дата последней поставки или отгрузки')

    def __str__(self):
        return self.productName

    class Meta:
        verbose_name = 'База данных'
        verbose_name_plural = 'Базы данных'
