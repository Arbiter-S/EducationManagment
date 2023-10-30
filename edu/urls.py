from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("administration/", admin.site.urls),
    path("",include("user.urls"))
]