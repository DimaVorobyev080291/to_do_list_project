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
    term = models.DateTimeField(verbose_name='Срок')
    status = models.CharField(max_length=50, verbose_name='Статус', choices=status_choices, default='Не выполнено')
    # tag
    created_at = models.DateTimeField(auto_now_add=True,  verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Дата изменения')

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'

    def __str__(self):
        return self.heading
