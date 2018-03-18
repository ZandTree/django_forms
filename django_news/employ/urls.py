from django.conf.urls import url
from employ import views

app_name = 'employ'
urlpatterns = [
    url(r'^$',views.index,name ='index'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^holiday/$',views.holiday,name='holiday'),
    url(r'^calender/$',views.calender,name='calender'),
]
