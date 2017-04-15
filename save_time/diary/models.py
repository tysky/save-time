from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day(models.Model):

    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    frog = models.ForeignKey('Frog', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.date)


class Frog(models.Model):

    name = models.CharField(max_length=200, help_text="Eat your frog!")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name