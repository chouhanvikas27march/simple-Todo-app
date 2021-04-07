from django.db import models

# Create your models here.
TASK_STATUS =(
    ('Complete','Complete'),
    ('Panding', 'Panding'),
    ('Running', 'Running'),
)

class AddtaskForm(models.Model):
    Project  = models.CharField(max_length=100)
    Task = models.CharField(max_length=100)
    Start_Date = models.DateField()
    Deadline = models.DateField(auto_now_add=True)
    Description = models.TextField()
    Status = models.CharField(choices=TASK_STATUS , max_length=10)

    def __str__(self):
        return self.Project