from django.db import models
from django.utils import timezone

class ActivityCategory(models.Model):
    category_name = models.CharField(max_length=32)

class Activity(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateField(default=timezone.now, blank=True, null=True)
    completed_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    note = models.TextField(blank=True, null=True)
    priority = models.PositiveIntegerField(blank=True, null=True)
    category = models.ManyToManyField(ActivityCategory, default=None)
    recurring_task = models.BooleanField(default=False) # if daily, completion will be logged and reset each day

    def __str__(self):
        return self.name

class Accomplishments(models.Model):
    #this is for tracking daily completion
    number_completed = models.PositiveSmallIntegerField() #score
    date = models.DateField(blank=True, null=True)
    activities = models.ManyToManyField(Activity)
