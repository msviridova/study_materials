from django.db import models


class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300, verbose_name='Название книги')
    author = models.ManyToManyField('Author', default='no author', verbose_name='Автор')
    description = models.TextField(blank=True, verbose_name='Описание')
    pages = models.IntegerField(blank=True, verbose_name='Количество страниц')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['-id']


class Author(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Имя автора')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
        ordering = ['name']


class Tag(models.Model):
    tag = models.CharField(max_length=150, db_index=True, verbose_name='Тэг')

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['tag']
