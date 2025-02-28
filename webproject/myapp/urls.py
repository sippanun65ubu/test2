
from django.urls import path, include
from .views import CourseListView,course_idsearch, course_namesearch,editcourseview,CourseDeleteView
urlpatterns = [
    path("course/", CourseListView.as_view(),name="course_list"),
    path("search/", course_idsearch,name="search_id"),
    path("namesearch/",course_namesearch, name="search_name"),
    path("course/update/<str:pk>", editcourseview.as_view(),name="update_course"),
    path("course/delete/<str:pk>", CourseDeleteView.as_view(), name="delete_course")
]
