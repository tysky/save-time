from django.db import models

# Create your models here.
class Frog(models.Model):

    name = models.CharField(max_length=200, help_text="Eat your frog!")

    def __str__(self):
        return self.name