from django.contrib import admin

from .models import *

class MajorAdmin(admin.ModelAdmin):
    list_display = ("name", "department", "academic_department", "units_number", "degree")
    search_fields = ("name", "department__name") 
    list_per_page = 20

admin.site.register(Department)
admin.site.register(Major, MajorAdmin)