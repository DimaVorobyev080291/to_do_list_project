from django.db import models

class To_do_list(models.Model):
    """
    Создаем таблицу to_do_list(Список дел)
    """
    status_choices = [
        ('Не выполнено', 'Не выполнено'),
        ('Выполнено', 'Выполнено'),
    ]

    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(max_length=3000, verbose_name='Описание', null=True, blank=True)
    term = models.DateTimeField(verbose_name='Срок', null=True, blank=True)
    status = models.CharField(max_length=50, verbose_name='Статус', choices=status_choices, default='Не выполнено')
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.heading
    
class Tags(models.Model):
    """
    Создаем таблицу тем Tags(теги) связанную с таблицей статей to_do_list(список дел)
    тип связи 'Многие-Ко-Многим'
    """
    title = models.CharField(max_length=50, unique=True, verbose_name='название')
    tags = models.ManyToManyField(To_do_list, through='To_do_listTags', related_name='tag', verbose_name='Тег')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
    
    def __str__(self):
        return self.title


class To_do_listTags(models.Model):
    """
    Промежуточная таблица для связи Многие-Ко-Многим между To_do_list и Tags
    """
    to_do = models.ForeignKey(To_do_list, on_delete=models.CASCADE, verbose_name='Список дел', related_name='to_do_list')
    tags = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Тег', related_name='tag_list')

    def __str__(self):
        return f'{self.to_do}_{self.tags}'

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связи'
