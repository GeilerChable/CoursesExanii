from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Course
from .forms import InscriptionStudent

def index(request):
    latest_course_list = Course.objects.all()
    return render(request, "exani/index.html", {
        "latest_course_list": latest_course_list
    })

def math(request):
    return render(request, "exani/math.html") 

def english(request):
    return render(request, "exani/english.html")

def espanol(request):
    return render(request, "exani/spanish.html")

def inscription(request):
    if request.method == "POST":
        form = InscriptionStudent(request.POST)
        if form.is_valid():
            form.save()
        return redirect('exani/inscription.html')
    else:
        form = InscriptionStudent()
    
    return render(request, 'exani/inscription_form.html', {'form': form})

#def detail(request, course_id):
#    course = get_object_or_404(Course, pk=course_id)
#    return render(request, "exani/detail.html", {
#        "course": course
#    })

def results(request, course_id):
    return HttpResponse(f"Estas viendo los temas del Curso número {course_id}")

def students(request, student_id):
    return HttpResponse(f"El número de estudiantes es de {student_id}")