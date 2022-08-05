from django.db import models


class Questions(models.Model):
    num_question = models.IntegerField(verbose_name='Номер вопроса')
    question = models.TextField(verbose_name='Текст вопроса')
    var_answers = models.ManyToManyField('Answers')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['num_question']

    def __str__(self):
        return str(self.num_question)


class Answers(models.Model):
    alco_type = models.CharField(max_length=100, verbose_name='Тип алкоголя', blank=True)
    answer = models.CharField(max_length=300, verbose_name='Ответ')
    weight_answer = models.IntegerField(verbose_name='Количество баллов за вопрос')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        ordering = ['weight_answer']

    def __str__(self):
        return self.answer


class Results(models.Model):
    result = models.IntegerField(verbose_name='Общее количество баллов')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
