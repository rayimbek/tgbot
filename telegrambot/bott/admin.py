from django.contrib import admin
from .models import *
# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        "email","first_name", "surname", "telephone", "password",

    ]
admin.site.register(CustomUser, CustomUserAdmin)

