from django.shortcuts import render
from django.views.generic import *
from .models import Course
from django.urls import reverse_lazy

# Create your views here.
class CourseListView(ListView):
    model = Course
    template_name = "course_list2.html"
    context_object_name = "course"

def course_idsearch(request):
    search = request.GET.get("code",'')
    course = Course.objects.filter(Course_id=search)
    return render(request, "course_search.html",{'course':course})


def course_namesearch(request):
    search = request.GET.get("code","")
    coursename = Course.objects.filter(Course_name=search)
    return render(request, "course_namesearch.html",{"course":coursename})

class editcourseview(UpdateView):
    model = Course
    fields = ("Course_name","name")
    context_object_name = "form"
    success_url = reverse_lazy('course_list')
    template_name = "update_course.html"

class CourseDeleteView(DeleteView):
    model = Course
    template_name = "delete_course.html"
    context_object_name = "course"
    success_url = reverse_lazy("course_list")
