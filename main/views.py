from django.shortcuts import render

from main.models import Banner, Class, Image, Student
from results.models import Examination

# Create your views here.
def home(request):
    """View function for home page of the site."""
    # Count of classes, students, and examinations
    num_classes = Class.objects.count()
    num_students = Student.objects.count()
    num_exams = Examination.objects.count()
    banners = Banner.objects.all()
    
    # Get the most recent examinations
    recent_exams = Examination.objects.order_by('-start_date')[:5]

    # Fetch a specific image (e.g., image with title 'School Logo')
    try:
        specific_image = Image.objects.get(title='Madrasa_Logo')
    except Image.DoesNotExist:
        specific_image = None

    context = {
        'num_classes': num_classes,
        'num_students': num_students,
        'num_exams': num_exams,
        'recent_exams': recent_exams,
        'specific_image': specific_image,
        'banners': banners,
    }
    
    return render(request, 'main/home.html', context=context)
