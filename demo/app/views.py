from django.shortcuts import render, redirect
from app.models import prdct,idgen
from django.core.files.storage import FileSystemStorage
def add(request):
    data1 = idgen.objects.get(id=1)
    id = data1.p_id
    id = int(id+1)
    p_id = "PNO_00" + str(id)
    request.session["p_id"] = id
    return render(request,"addp.html",{'p_id':p_id})
       
    
    return render(request,"addp.html")
def addpf(request):
    if request.method=='POST':
        data=prdct()
        data.p_id=request.POST.get('id')
        data.p_name=request.POST.get('name')
        data.p_price=request.POST.get('price')
        Photo = request.FILES['photo']
        fs = FileSystemStorage()
        filename = fs.save(Photo.name, Photo) 
        uploaded_file_url = fs.url(filename)
        data.p_pic=uploaded_file_url
        data.save()
        data1=idgen.objects.get(id=1)
        data1.p_id=request.session['p_id']
        data1.save()
        
        return render(request,"addp.html")
def homef(request):
    return render(request,"home.html")
def viewpf(request):
    data=prdct.objects.all()
    return render(request,"viewp.html",{'data1':data})
def remove(request):
    data=prdct.objects.all()
    return render(request,"removep.html",{'data1':data})
def removepf(request,id1):
    data=prdct.objects.get(p_id=id1)
    data.delete()
    return redirect('/removep')
def updatedata(request,id1):
    data=prdct.objects.get(p_id=id1)
    return render(request,"update.html",{'data1':data})
def update1(request,id2):
    data=prdct.objects.get(p_id=id2)  
    data.p_name=request.POST.get('name')
    data.p_price=request.POST.get('price')
    photo = request.FILES['photo']
    fs = FileSystemStorage()
    filename = fs.save(photo.name,photo) 
    uploaded_file_url = fs.url(filename)
    data.p_pic=uploaded_file_url
    data.save()
    return redirect('/viewp')
def orderprof(request):
    data1 = idgen.objects.get(id=1)
    id = data1.o_id
    id = int(id+1)
    o_id = "ONO_00" + str(id)
    request.session["o_id"] = id
    d=prdct.objects.all()
    return render(request,"odr.html",{'o_id':o_id,'d':d})
def ordrf(request):
    if request.method=='POST':
        data=prdct()
        data.o_id=request.POST.get('id')
        data.p_id_id=request.POST.get('product')
        data.o_date=request.POST.get('date')
        data.o_qnty=request.POST.get('quantity')
        data.o_sts=request.POST.get('status')
        data.save()
        data1=idgen.objects.get(id=1)
        data1.o_id=request.session['o_id']
        data1.save()
        
        return render(request,"odr.html")

# Create your views here.
