from django.db import models
from tasks.models import Project, Task


class BugReport(models.Model):
    New = 'New'
    In_progress = 'In_progress'
    Completed = 'Completed'
    STATUS_CHOICES = [
        (New, 'Новая'),
        (In_progress, 'В работе'),
        (Completed, 'Завершена')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='BugReports',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='BugReports',
        on_delete=models.SET_NULL,
        null = True,
        blank = True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='New'
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FeatureRequest(models.Model):
    STATUS_CHOICES = [
        ('Consideration', 'Рассмотрение'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено')
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        Project,
        related_name='FeatureRequest',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        Task,
        related_name='FeatureRequest',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_CHOICES,
        default='Consideration'
    )
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)