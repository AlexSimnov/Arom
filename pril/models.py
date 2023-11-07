from django.db import models


class Product(models.Model):
    #
    name = models.CharField(
        'Название',
        max_length=150,
        null=False,
        blank=False,
    )
    amount = models.PositiveSmallIntegerField(
        'Количество',
    )
    date_priv = models.DateField(
        'Дата поставки',
        auto_now_add=True,
    )
    date_snat = models.DateField(
        'До какого числа',
        null=False,
        blank=False,
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        ordering = ['date_snat']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Planogram(models.Model):
    date_add = models.DateField(
        'дата добавления',
    )
    image = models.ImageField()

    class Meta:
        verbose_name = 'Планограмма'
