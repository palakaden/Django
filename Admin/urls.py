from django.urls import path,include
from Admin import views
app_name="webadmin"
urlpatterns = [
     path("district/",views.district,name="district"),
     path("category/",views.category,name="category"),
     path("Deletedistrict/<int:did>",views.deldistrict,name="deldistrict"),
     path("Editdistrict/<int:eid>",views.editdistrict,name="editdistrict"),
     path("Deletecategory/<int:did>",views.delcategory,name="delcategory"),
     path("Editcategory/<int:eid>",views.editcategory,name="editcategory"),
]