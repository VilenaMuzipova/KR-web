from django.db import models

# Create your models here.

class ToDoList(models.Model):
    id = models.CharField(
        max_length=120,
        verbose_name='Номер'
    )
    to_do = models.CharField(
        max_length=120,
        verbose_name='начать бегать по утрам'
    )
    done = models.CharField(
        max_length=120,
        verbose_name='Выполнено'
    )
    created_at = models.IntegerField(
        max_length=120,
        verbose_name='Создано на',
        default = 1,
    )
    until_date = models.DateField(
        auto_now = True,
        max_length=120,
        verbose_name='2022-10-31'
    )

    def __str__(self):
        return f'Name:{self.name} {self.thing}'
