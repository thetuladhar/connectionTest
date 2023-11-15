from django.db import models
from django.urls import reverse
# Create your models here.

#Create a Task model with fields for title, description, due_date, and status.
class Task(models.Model):
    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def get_absolute_url(self):
        return reverse('task_detail', args=[str(self.id)])

    def __str__(self):
        return self.title