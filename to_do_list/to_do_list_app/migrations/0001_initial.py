# Generated by Django 5.1.4 on 2024-12-13 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='To_do_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание')),
                ('term', models.DateTimeField(verbose_name='Срок')),
                ('status', models.CharField(choices=[('Выполнено', 'Выполнено'), ('Не выполнено', 'Не выполнено')], max_length=50, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'Список дел',
                'verbose_name_plural': 'Список дел',
            },
        ),
    ]
