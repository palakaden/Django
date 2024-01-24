from django.shortcuts import render
from Admin.models import*
# Create your views here.

def district(request):
    if request.method=="POST":
        tbl_district.objects.create(district_name=request.POST.get("dst")),
        return render(request,"Admin/district.html")
    else:
        return render(request,"Admin/district.html")

