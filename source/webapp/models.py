from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = models.TextField(max_length=2000,null=False,blank=False, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', related_name='tasks', on_delete=models.PROTECT, verbose_name='Тип')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.summary

class Status(models.Model):
    status = models.CharField(max_length=30, verbose_name='Статус')

    def __str__(self):
        return self.status

class Type(models.Model):
    type = models.CharField(max_length=30, verbose_name='Тип')

    def __str__(self):
        return self.type
