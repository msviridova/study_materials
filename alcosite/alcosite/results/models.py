from django.db import models


class Results(models.Model):
    result = models.IntegerField(verbose_name='Общее количество баллов')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
