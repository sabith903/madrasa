from django.db import models

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=50)  # e.g., "Class 10A", "Grade 12 Science"
    year = models.CharField(max_length=100) # e.g., "2021-2022", "2022-2023"
    
    def __str__(self):
        return f"{self.name} - {self.year}"
    
    class Meta:
        verbose_name_plural = "Classes"
        unique_together = ('name', 'year')
        
class Student(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    roll_number = models.CharField(max_length=20)  # Removed unique=True
    class_enrolled = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='students')
    reg_number = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return f"{self.name} ({self.reg_number})"
    
    class Meta:
        # This makes roll_number unique only within a class
        unique_together = ['roll_number', 'class_enrolled']
        
        

class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')  # Saved inside `/media/images/`

    def __str__(self):
        return self.title
    
class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='banners/')  # Saved inside `/media/banners/`

    def __str__(self):
        return self.title