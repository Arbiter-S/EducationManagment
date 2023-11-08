from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import StudentCourse


@receiver(post_save, sender=StudentCourse)
def set_pass_or_fail(sender, instance, created, **kwargs):
    if created:
        if instance.score >= 10:
            instance.pass_or_fail = "P"  # "P"
        else:
            instance.pass_or_fail = "F"  # "F"
        instance.save()
