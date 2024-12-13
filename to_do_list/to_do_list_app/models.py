from django.db import models

class To_do_list(models.Model):
    """
    Создаем таблицу to_do_list(Список дел)
    """
    status_choices = [
        ('Выполнено', 'Выполнено'),
        ('Не выполнено', 'Не выполнено'),
    ]

    heading = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.CharField(max_length=255, verbose_name='Описание', null=True, blank=True)
    term = models.DateTimeField(verbose_name='Срок')
    status = models.CharField(max_length=50, verbose_name='Статус', choices=status_choices)
    # tag
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.heading
