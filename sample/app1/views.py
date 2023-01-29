from django.shortcuts import redirect, render
from app1.models import dept
def home(request):
    return render(request,"page1.html")
def homef(request):
    return render(request,"home.html")

def aboutf(request):
    return render(request,"about.html")
def contactf(request):
    return render(request,"contact.html")
def loginf(request):
    return render(request,"login.html")
def regf(request):
    return render(request,"reg.html")
def studentf(request):
    return render(request,"student.html")
def indexf(request):
    return render(request,"index.html")
def galleryf(request):
    return render(request,"gallery.html")
def about1f(request):
    return render(request,"about1.html")
def insert(request):
    if request.method=='POST':
        n1=request.POST.get('id')
        n2=request.POST.get('name')
        n3=request.POST.get('dept')
        n4=int(request.POST.get('m1'))
        n5=int(request.POST.get('m2'))
        n6=int(request.POST.get('m3'))
        n7=int(request.POST.get('m4'))
        sum=n4+n5+n6+n7
        avg=sum/4
        return render(request,"viewdata.html",{'data':n1,'data2':n2,'data3':n3,'data4':sum,'data5':avg,'data6':avg})
def deptf(request):
    return render(request,"dept.html")
def insertionf(request):
    if request.method=='POST':
        data=dept()
        data.dept_id=request.POST.get('id')
        data.name=request.POST.get('name')
        data.save()
        return render(request,"dept.html")
def viewdata1f(request):
    data=dept.objects.all()
    return render(request,"viewdata1.html",{'data1':data})

def removedeptf(request,id1):
    data=dept.objects.get(dept_id=id1)
    data.delete()
    return redirect('/viewdata1')


# Create your views here.
