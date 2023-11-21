from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)

urlpatterns = [
    path("administration/", admin.site.urls),
    path("", include("user.urls")),
    path("", include("department.urls")),
    path("", include("course.urls")),
    path("", include("university.urls")),
    path("", include("course_selection.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="redoc"), name="redoc"),
]
