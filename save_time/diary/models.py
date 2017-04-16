from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Day(models.Model):
    """
    Day model represent one page of business diary which consist of date, tasks,
    frogs, steak, main task of the day (challenge), main event of the day (for memory),
    awards for completing tasks.
    """
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.date)


class Challenge(models.Model):
    """
    Model for main task of the day.
    """
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Model for tasks of the day. Include hard and flexible tasks.
    """
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    TASK_TYPE = (
        ('f', 'Flexible'),
        ('h', 'Hard'),
    )
    task_type = models.CharField(max_length=1, choices=TASK_TYPE, default='f')
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Frog(models.Model):
    """
    Start your day with some frogs.
    """
    name = models.CharField(max_length=200, help_text="Eat your frog!")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    done = models.BooleanField(default=False)
    day = models.ManyToManyField(Day, blank=True)

    def __str__(self):
        return self.name


class Steak(models.Model):
    """
    You can cut your big work into steaks and eat one steak per day.
    """
    name = models.CharField(max_length=200, help_text="Cut your elephant into small steaks")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Joy(models.Model):
    """
    Your awards of the day.
    """
    name = models.CharField(max_length=200, help_text="Take your award")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Memory(models.Model):
    """
    Represent main event of the day, week, month, year.
    It helps you to define your life goals.
    """
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    day = models.ForeignKey(Day, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


