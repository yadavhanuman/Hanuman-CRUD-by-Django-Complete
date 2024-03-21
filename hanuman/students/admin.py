from django.contrib import admin
from.models import *

@admin.register(register)

class studentsAdmin(admin.ModelAdmin):
    list_display=('name','age','phone','mail')

# Register your models here.
