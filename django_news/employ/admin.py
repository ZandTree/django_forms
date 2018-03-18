from django.contrib import admin
from .models import Employee,Holiday,My_calender

# Register your models here.
admin.site.register(Employee)
admin.site.register(Holiday)
admin.site.register(My_calender)
