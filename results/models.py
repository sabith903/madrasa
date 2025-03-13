from django.db import models  
from main.models import Student

# Create your models here.
class Examination(models.Model):
    name = models.CharField(max_length=100)  # e.g., "Final Exam", "Mid-term"
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"
    
class Result(models.Model):
    RESULT_CHOICES = (
        ('PASS', 'Pass'),
        ('FAIL', 'Fail'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    examination = models.ForeignKey(Examination, on_delete=models.CASCADE, related_name='results')
    status = models.CharField(max_length=4, choices=RESULT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('student', 'examination')
    
    def __str__(self):
        return f"{self.student.name} - {self.examination.name}: {self.status}"