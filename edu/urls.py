from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("administration/", admin.site.urls),
    path("", include("user.urls")),
    path("", include("department.urls")),
    path("", include("course.urls")),
    path("", include("university.urls")),
    path("",include("course_selection.urls")),
]
