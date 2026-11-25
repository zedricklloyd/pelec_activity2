from django.shortcuts import render, get_object_or_404, redirect
from .models import Student


def student_list(request):
    students = Student.objects.all().order_by('last_name')

    return render(request, 'students/student_list.html', {
        'students': students
    })


def student_profile(request, pk):
    students = Student.objects.all()
    student = get_object_or_404(Student, pk=pk)

    return render(request, 'students/student_profile.html', {
        'students': students,
        'student': student
    })


def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            student_id=request.POST.get('student_id'),
            first_name=request.POST.get('first_name'),
            middle_name=request.POST.get('middle_name'),
            last_name=request.POST.get('last_name'),
            birthdate=request.POST.get('birthdate'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address'),
            previous_school=request.POST.get('previous_school'),
            father_name=request.POST.get('father_name'),
            mother_name=request.POST.get('mother_name'),
            guardian=request.POST.get('guardian'),
            course=request.POST.get('course'),
            year_level=request.POST.get('year_level'),
            section=request.POST.get('section'),
            school_year=request.POST.get('school_year'),
            semester=request.POST.get('semester'),
            enrollment_status=request.POST.get('enrollment_status')
        )

        return redirect('students:student_list')

    return render(request, 'students/add_student.html')