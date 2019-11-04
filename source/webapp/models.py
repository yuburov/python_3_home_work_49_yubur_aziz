from django.db import models

class Task(models.Model):
    summary = models.CharField(max_length=200, verbose_name='Краткое описание')
    description = models.TextField(max_length=2000,null=True,blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('webapp.Status', related_name='tasks', on_delete=models.PROTECT, verbose_name='Статус')
    type = models.ForeignKey('webapp.Type', related_name='tasks', on_delete=models.PROTECT, verbose_name='Тип')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    project = models.ForeignKey('webapp.Project', null= True, blank=False, related_name='tasks', on_delete=models.PROTECT,verbose_name='Проект')

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

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название проекта')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание проекта')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    update_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
       return self.name

class Team(models.Model):
    user = models.ForeignKey('auth.User', related_name='user_projects', on_delete=models.CASCADE,
                             verbose_name='Пользователь')
    project = models.ForeignKey('webapp.Project', related_name='project_users', on_delete=models.CASCADE,
                                verbose_name='Проект')
    start_date = models.DateField(verbose_name='Дата начала работы')
    end_date = models.DateField(verbose_name='Дата окончания работы')

    def __str__(self):
        return "{} | {}".format(self.user, self.project)
    