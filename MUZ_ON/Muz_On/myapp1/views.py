from django.shortcuts import render
from myapp1.models import Worker, Specialte, Time


def index_page(request):

    return render(request, 'index.html')

def about_page(request):

    return render(request, 'about.html')

def timing_page(request):
    all_time = Time.objects.all()
    return render(request, 'timing.html', context={'data3': all_time})

def teacher_page(request):

    all_workers = Worker.objects.all()

    return render(request, 'teacher.html', context={'data': all_workers})

def profession_page(request):
    all_specialte = Specialte.objects.all()
    return render(request, 'profession.html', context={'data2': all_specialte})

def write_page(request):

    return render(request, 'write.html')