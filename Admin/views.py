from django.shortcuts import render
from Admin.models import*
# Create your views here.

def district(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("dst")),
        return render(request,"Admin/district.html",{"district": districtdata})
    else:
        return render(request,"Admin/district.html")

def category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("cat")),
        return render(request,"Admin/category.html",{"category": categorydata})
    else:
        return render(request,"Admin/category.html")

