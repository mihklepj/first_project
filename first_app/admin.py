from django.contrib import admin
from .models import Student, StudentAdmin, Teacher, Subject

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Subject)