from django.db import models
import calendar

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30,help_text='first name')
    PROF_CHOICES = (
        ('CLEANER','cleaning dep'),
        ('KITCHEN','people from kitchen dep'),
        ('PILOT','spaceship pilot'),
        ('DOCTOR','person treating people'),
    )
    # 1.если поменять\добавить что-то типа default = "UNEMPLOYED",то не нужна миграция, layout get autm adjusted
    #2. без default в models.py и попытке прописать в соответ-ей forms.ModelForm  widgets = {'prof':forms.RadioSelect,}
    # появится в строках не только PROF_CHOICES[1] = cleaning dep, f starnge line ---

    prof = models.CharField(max_length=20,choices=PROF_CHOICES,default = PROF_CHOICES[0])

    #prof = models.CharField(max_length = 20,choices = PROF_CHOICES,default = "")
    # this method ==> still unclear to me (get "name 'ValidationError' is not defined" in shell by .clean() or .full_clean()
    def clean(self):
        if ('Joker' in self.name) and (self.prof == 'DOCTOR'):
            raise ValidationError('Get out of here!')


    def __str__(self):
        return self.name

class Holiday(models.Model):
    MONTH_CHOICES = (
        ('JAN','JANUARY'),
        ('FEB','FEBUARY'),
        ('MAR','MARCH'),
        ('APR','APRIL'),
        ('MAY','MY BEST MONTH')
    )
    month = models.CharField(max_length=20,choices = MONTH_CHOICES,default = MONTH_CHOICES[0])

# Этот класс доработать, ничего не видно в layout-e
class My_calender(models.Model):
    MONTH_CHOICES  = [(str(i),calendar.month_name[i]) for i in range(1,13)]
    month = models.CharField(max_length=15,choices=MONTH_CHOICES,default='1')
