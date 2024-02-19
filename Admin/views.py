from django.shortcuts import render,redirect
from Admin.models import*
# Create your views here.

def district(request):
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("dst")),
        return render(request,"Admin/district.html",{"district": districtdata})
    else:
        return render(request,"Admin/district.html",{"district": districtdata})

def category(request):
    categorydata=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get("cat")),
        return render(request,"Admin/category.html",{"category": categorydata})
    else:
        return render(request,"Admin/category.html",{"category": categorydata})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:district")

def editdistrict(request,eid):
    data=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        data.district_name=request.POST.get("dst")
        data.save()
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/district.html",{"edit": data})
    
def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("webadmin:category")

def editcategory(request,eid):
    data=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        data.category_name=request.POST.get("cat")
        data.save()
        return redirect("webadmin:category")
    else:
        return render(request,"Admin/category.html",{"edit": data})
