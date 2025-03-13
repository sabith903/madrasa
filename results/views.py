from django.shortcuts import get_object_or_404, render

from main.models import Class, Student
from results.models import Examination, Result

# Create your views here.
def result_class_list(request):
    """Display a list of all classes"""
    classes = Class.objects.all().order_by('year', 'name')
    classes = sorted(classes, key=lambda x: int(x.name) if x.name.isdigit() else x.name)
    context = {'classes': classes}
    return render(request, 'results/result_class_list.html', context)

def class_passed_students(request, class_id):
    """
    Show students from a specific class who passed the latest examination
    """
    class_obj = get_object_or_404(Class, id=class_id)
    
    # Find the latest examination
    latest_exam = Examination.objects.order_by('-end_date').first()
    
    if latest_exam:
        # Get students from this class who passed the latest examination
        passed_students = Student.objects.filter(
            class_enrolled=class_obj,
            results__examination=latest_exam,
            results__status='PASS'
        ).order_by('name')
        
        # Create a list of students with their result status
        students_with_status = []
        for student in passed_students:
            # Get the specific result for this student and examination
            result = Result.objects.get(student=student, examination=latest_exam)
            students_with_status.append({
                'student': student,
                'status': result.status
            })
        
        context = {
            'class': class_obj,
            'latest_exam': latest_exam,
            'passed_students': students_with_status
        }
    else:
        context = {
            'class': class_obj,
            'latest_exam': None,
            'passed_students': []
        }
    
    return render(request, 'results/class_passed_students.html', context)