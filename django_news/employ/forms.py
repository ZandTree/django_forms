from django import forms
from employ.models import Employee,Holiday,My_calender

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        #fields = '__all__'
        fields =['name','prof']
        widgets = {'prof':forms.RadioSelect,}

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = '__all__'
        widgets = {'month':forms.RadioSelect,}

class CalenderForm(forms.ModelForm)   :
    class Meta:
        model = My_calender
        fields = '__all__'
        widgets = {'month':forms.RadioSelect,} 
