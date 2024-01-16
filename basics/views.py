from django.shortcuts import render

# Create your views here.
def sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt1"))
        num2=int(request.POST.get("txt2"))
        sum=num1+num2
        return render(request,"basics/sum.html",{"Result":sum})
    else:
        return render(request,"basics/sum.html")
def calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("txt1"))
        num2=int(request.POST.get("txt2"))
        click=request.POST.get("save")
        if click=="+":
            sum=num1+num2
        elif click=="-":
            sum=num1-num2
        elif click=="*":
            sum=num1*num2
        else:
            sum=num1/num2        
        return render(request,"basics/calculator.html",{"Result":sum})
    else:
        return render(request,"basics/calculator.html")
def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("txt1"))
        b=int(request.POST.get("txt2"))
        c=int(request.POST.get("txt3"))
        if a>=b and a>=c:
            largest=a
        elif b>=a and b>=c:
            largest=b
        else:
            largest=c

        if a<b and a<c:
            smallest=a
        elif b<a and b<c:
            smallest=b
        else:
            smallest=c
        return render(request,"basics/largest.html",{"Largest":largest,"Smallest":smallest})
    else:
        return render(request,"basics/largest.html")





def bsalary(request):
    if request.method=="POST":
        fname=request.POST.get("txtname")
        lname=request.POST.get("txtname1")
        gender=request.POST.get("txtgender")
        martial=request.POST.get("txtmartial")
        department=request.POST.get("dpt")
        basicsalary=int(request.POST.get("txtbasic"))
        if gender=="MALE":
            result="Mr "+fname+" "+lname
            
        else:
            result="Mrs "+fname+" "+lname
            
        if gender=="MALE":
            gen="Malw"
        else:
            gen="Female"

        if martial=="Single":
            mar="Single"
        else:
            mar="Married"

        if department=="cs":
            dep="Computer Science"
        elif department=="it":
            dep="Information Technology"
        else:
            dep="Medical"
        
        if basicsalary>=10000:
            TA=basicsalary*(40/100)
            DA=basicsalary*(35/100)
            HRA=basicsalary*(30/100)
            LIC=basicsalary*(25/100)
            PF=basicsalary*(20/100)
        elif basicsalary>=5000:
             TA=basicsalary*(35/100)
             DA=basicsalary*(30/100)
             HRA=basicsalary*(25/100)
             LIC=basicsalary*(20/100)
             PF=basicsalary*(15/100)
        else:
             TA=basicsalary*(30/100)
             DA=basicsalary*(25/100)
             HRA=basicsalary*(20/100)
             LIC=basicsalary*(15/100)
             PF=basicsalary*(10/100)
        Dedu=LIC+PF
        Net=basicsalary+TA+DA+HRA-(LIC+PF)                           
        return render(request,"basics/bsalary.html",{"Name":result,"Gender":gen,"Martial":mar,"Dep":dep,"Basic":basicsalary,"Ta":TA,"Da":DA,"Hra":HRA,"Lic":LIC,"Pf":PF,
                                                     "Deduction":Dedu,"NET":Net})
        
    else:
        return render(request,"basics/bsalary.html")