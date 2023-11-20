from django.urls import path

from .views import *

urlpatterns = [
    path("terms/", TermAPIListView.as_view(), name="term_list_view"),
    path("term/<str:pk>/", TermAPIDetailView.as_view(), name="term_detail_view"),
]
