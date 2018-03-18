from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm,HolidayForm,My_calender

# Create your views here.
def index(request):
    list_em = Employee.objects.order_by('name')
    return render(request,'employ/index.html',{'em':list_em})

def contact(request):
    form1 = EmployeeForm()
    return render(request,'employ/contact.html',{'form1':form1})

def holiday(request):
    form2 = HolidayForm()
    return render(request,'employ/holiday.html',{'form2':form2})

def calender(request):
    form = My_calender()
    return render(request,'employ/calender.html',{'form':form})    
