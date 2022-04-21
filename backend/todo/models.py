from django.db import models

class TodoCategory(models.Model) :
    name = models.CharField(max_length=255, unique=True)

class Todo(models.Model):
    title = models.CharField(max_length=255, default='Something to do')
    category = models.ForeignKey(to=TodoCategory, on_delete=models.PROTECT)
