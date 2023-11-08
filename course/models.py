from django.db import models
from multiselectfield import MultiSelectField

TYPE_CHOICES = (
    ("G", "General"),
    ("R", "Required"),
    ("C", "Core"),
    ("O", "Optional"),
)

DAYS_CHOICES = (
    ("Mon", "Monday"),
    ("Tue", "Tuesday"),
    ("Wed", "Wednesday"),
    ("Thu", "Thursday"),
    ("Fri", "Friday"),
    ("Sat", "Saturday"),
    ("Sun", "Sunday"),
)


class ApprovedCourse(models.Model):
    name = models.CharField(max_length=30)
    department = models.ForeignKey("department.Department", on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    unit = models.PositiveIntegerField()
    prerequisite = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="preapprovedcourse")
    corequisite = models.ManyToManyField("self", blank=True, symmetrical=False, related_name="coapprovedcourse")

    def __str__(self):
        return self.name


class SemesterCourse(models.Model):
    exam_date = models.DateTimeField(null=True, blank=True)
    exam_location = models.CharField(max_length=30, blank=True, null=True)
    class_days = MultiSelectField(max_length=15, choices=DAYS_CHOICES, null=True, blank=True)
    class_end_time = models.TimeField(null=True, blank=True)
    class_start_time = models.TimeField(null=True, blank=True)
    approved_course = models.ForeignKey("ApprovedCourse", on_delete=models.CASCADE)
    professor = models.ForeignKey("user.Professor", on_delete=models.CASCADE, null=True, blank=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.approved_course} {self.professor}"
