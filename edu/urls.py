from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("eduadmin/", admin.site.urls),
    path('admin/',include('user.urls'))
]