from django.db import models

class Variable(models.Model):
    name = models.CharField(max_length=32)
    value = models.IntegerField()
    def __str__(self):
        return self.name

class Member(models.Model):
    name = models.CharField(max_length=32)
    is_son = models.BooleanField(default=False)
    household_count =models.IntegerField()


    def __str__(self):
        return self.name





