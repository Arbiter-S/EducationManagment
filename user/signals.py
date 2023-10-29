from django.db.models.signals import post_save, pre_save 
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

from .models import *

import random

import string

@receiver(post_save, sender = User)
def password(sender, instance, **kwargs):
    if not instance.is_superuser:
        user_password = instance.password
        instance.password = make_password(user_password)

@receiver(post_save, sender = User)
def code(sender, instance, created, **kwargs):
    if created and not instance.user_code:
        code_length = 10
        code = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(code_length))
        if instance.role == "STU":
            instance.user_code = f"{instance.role}-{code}"
        elif instance.role == "PRO":
            instance.user_code = f"{instance.role}-{code}"
        elif instance.role == "AST":
            instance.user_code = f"{instance.role}-{code}"
        elif instance.role == "ADM":
            instance.user_code = f"{instance.role}-{code}"
        instance.save()

@receiver(pre_save, sender = Student)
def military(sender, instance, **kwargs):
    if instance.user.gender == "M":
        instance.military_status = instance.get_military_status()
    else:
        instance.military_status = None

@receiver(post_save, sender = ITAdmin)
def superuser(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        user.is_superuser = True
        user.is_staff = True
        user.save()