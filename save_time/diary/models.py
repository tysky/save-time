from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Frog(models.Model):

    name = models.CharField(max_length=200, help_text="Eat your frog!")
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name