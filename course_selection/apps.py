from django.apps import AppConfig


class CourseSelectionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_selection'

    def ready(self):
        import course_selection.signals
