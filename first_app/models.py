from django.db import models
from django.contrib import admin

# Create your models here.
class Student(models.Model):
    """ Student database table """
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)  # null: missing; blank: empty
    weight = models.IntegerField()

class StudentAdmin(admin.ModelAdmin):
    list_filter = ['weight']

    def birthday(self, obj):
        if obj.birth_date is not None:
            return obj.birth_date.strftime('%d.%m.%Y')

    list_display = ['name', 'weight', 'birthday']
    list_per_page = 10

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)


class Subject(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name} teaches {self.subject}'

class TeacherAdmin(admin.ModelAdmin):
    list_filter = ['subject']
    list_display = ['name', 'subject']
    list_per_page = 10