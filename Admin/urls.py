from django.urls import path,include
from Admin import views
urlpatterns = [
     path("district/",views.district),
]