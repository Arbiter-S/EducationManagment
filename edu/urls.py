from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenBlacklistView, TokenObtainPairView, TokenRefreshView

if settings.DEBUG:
    urlpatterns = [
        path("", include("user.urls")),
        path("", include("department.urls")),
        path("", include("course.urls")),
        path("", include("university.urls")),
        path("", include("course_selection.urls")),
        path("administration/", admin.site.urls),
        path("login/", TokenObtainPairView.as_view()),
        path("refresh/", TokenRefreshView.as_view()),
        path("logout/", TokenBlacklistView.as_view()),
        path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
        path("api/schema/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
        path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="redoc"), name="redoc"),
    ]
else:
    urlpatterns = [
        path("", include("user.urls")),
        path("", include("department.urls")),
        path("", include("course.urls")),
        path("", include("university.urls")),
        path("", include("course_selection.urls")),
        path("administration/", admin.site.urls),
        path("login/", TokenObtainPairView.as_view()),
        path("refresh/", TokenRefreshView.as_view()),
        path("logout/", TokenBlacklistView.as_view()),
    ]
