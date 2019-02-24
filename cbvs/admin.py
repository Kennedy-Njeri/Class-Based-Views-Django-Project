from django.contrib import admin
from cbvs.models import School, Student

# Register your models here.

admin.site.register(Student)
admin.site.register(School)