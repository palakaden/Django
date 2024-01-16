from django.urls import path,include
from basics import views
urlpatterns = [
     path("Addition/",views.sum),
     path("Calculator/",views.calculator),
     path("Largest/",views.largest),
     path("Bsalary/",views.bsalary),
]