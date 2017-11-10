from django.db import models

class Task_template(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Field_name(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(Type)
    task_template = models.ForeignKey(Task_template)
    def __str__(self):
        return self.name


