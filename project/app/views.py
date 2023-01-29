import email
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from app.models import tbl_cust_order, tbl_emp_duty, tbl_employee, tbl_leave_application, tbl_login, tbl_menu, tbl_payment, tbl_rest_stall, tbl_restaurent, tbl_review, tbl_stall,idgen,tbl_customer, tbl_table, tbl_tablebooking
import datetime
# Create your views here.
def home(request):
    return render(request,"index.html")

def loginf(request):
    return render(request,"login.html")

def regf(request):
    return render(request,"registration.html")
def forms(request):
    return render(request,"form.html")

def menubarf(request):
    return render(request,"menubar.html")

def admin_menubarf(request):
    return render(request,"admin_menubar.html")

def cust_menubar(request):
    return render(request,"cust_menubar.html")

def rest_menubarf(request):
    return render(request,"restaurantmenu_bar.html")

def addstall(request):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.stall_id
        id = int(id+1)
        stall_id = "STNO_00" + str(id)
        request.session["stall_id"] = id
        return render(request,"addstall.html",{'stall_id':stall_id})
    

            
def addstallf(request):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_stall()
            data.stall_id=request.POST.get('stall_id')
            data.stall_number=request.POST.get('stall_number')
            
            data.descripion=request.POST.get('descripion')
            data.status="Available"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.stall_id=request.session['stall_id']
            data1.save()
            
            return render(request,'adminhome.html')
    
def removestall(request):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_stall.objects.all()
        return render(request,"removestall.html",{'data1':data})

def removestall1(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_stall.objects.get(stall_id=id1)
        data.delete()
        return redirect('/removestall/')



def updatestall(request,id1):
    data=tbl_stall.objects.get(stall_id=id1)
    return render(request,"updatestall.html",{'data1':data})

def updatestall2(request,id2):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        if request.POST.get('photo')=="":

            data=tbl_stall.objects.get(stall_id=id2)  
            data.stall_number=request.POST.get('stall_number')
            photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(photo.name,photo) 
            uploaded_file_url = fs.url(filename)
            data.photo=uploaded_file_url
            data.descripion=request.POST.get('descripion')
            data.save()

        else:
            data=tbl_stall.objects.get(stall_id=id2)  
            data.stall_number=request.POST.get('stall_number')
            data.descripion=request.POST.get('descripion')
            data.save()

        return redirect('/removestall/')

def customerregistration(request):
    data1 = idgen.objects.get(id=1)
    id = data1.cust_id
    id = int(id+1)
    cust_id = "CTNO_00" + str(id)
    request.session["cust_id"] = id
    return render(request,"customerregistration.html",{'cust_id':cust_id})

def customerregistrationf(request):
    if request.method=='POST':
        data=tbl_customer()
        data.cust_id=request.POST.get('cust_id')
        data.cust_name=request.POST.get('cust_name')
        data.house_name=request.POST.get('house_name')
        data.street=request.POST.get('street')
        data.city=request.POST.get('city')
        data.district=request.POST.get('district')
        data.state=request.POST.get('state')
        data.pin_code=request.POST.get('pin_code')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.save()
        data1=idgen.objects.get(id=1)
        data1.cust_id=request.session['cust_id']
        data1.save()
        log=tbl_login()
        log.user_name=data.email
        log.password=data.phone
        log.cat="cust"
        log.save()

        
        return render(request,'index.html')

def restaurentregistration(request):
    data1 = idgen.objects.get(id=1)
    id = data1.rest_id
    id = int(id+1)
    rest_id = "RSTNO_00" + str(id)
    request.session["rest_id"] = id
    return render(request,"restaurentregistration.html",{'rest_id':rest_id})

def restaurentregistrationf(request):
    if request.method=='POST':
        data=tbl_restaurent()
        data. rest_id=request.POST.get('rest_id')
        data.rest_name=request.POST.get('rest_name')
        data.street=request.POST.get('street')
        data.city=request.POST.get('city')
        data.district=request.POST.get('district')
        data.state=request.POST.get('state')
        data.pin_code=request.POST.get('pin_code')
        data.particulers=request.POST.get('particulers')
        data.type=request.POST.get('type')
        data.rm_name=request.POST.get('rm_name')
        data.phone=request.POST.get('phone')
        data.email=request.POST.get('email')
        data.status="Not verified"
        data.save()
        data1=idgen.objects.get(id=1)
        data1.rest_id=request.session['rest_id']
        data1.save()
        log=tbl_login()
        log.user_name=data.rest_id
        log.password=data.phone
        log.cat="rest"
        log.save()
        
        return render(request,'index.html')

def restappscn(request):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_restaurent.objects.filter(status="Not verified")
        return render(request,"verifyrest.html",{'data1':data})

def verifyrest1(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_restaurent.objects.get(rest_id=id1)
        return render(request,"verifyrest1.html",{'data':data})

def accept(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_restaurent.objects.get(rest_id=id1)
        data.status="verified"
        data.save()
        log=tbl_login()
        log.user_name=data.rest_id
        log.password=data.phone
        log.cat="rest"
        log.save()
        return redirect('/restappscn/')

def reject(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_restaurent.objects.get(rest_id=id1)
        data.status="Rejected"
        data.save()
        return redirect('/restappscn/')



def addmenu(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.menu_id
        id = int(id+1)
        menu_id = "MENU_00" + str(id)
        request.session["menu_id"] = id
        return render(request,"addmenu.html",{'menu_id':menu_id})

def addmenuf(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_menu()
            data.menu_id=request.POST.get('menu_id')
            data.menu_name=request.POST.get('menu_name')
            data.rest_id_id=request.session['rest']
            data.description=request.POST.get('description')
            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.photo=uploaded_file_url
            data.unit=request.POST.get('unit')
            data.quantity=request.POST.get('quantity')
            data.price=request.POST.get('price')
            data.save()
            data1=idgen.objects.get(id=1)
            data1.menu_id=request.session['menu_id']
            data1.save()
            
            return render(request,'resthome.html')

def loginf(request):
        return render(request,'login.html')
def adminhome(request):
        return render(request,'admin_menubar.html')
def custhome(request):
        return render(request,'cust_menubar.html')
def resthome(request):
        return render(request,'resthome.html')
def employeehome(request):
        return render(request,'employeehome.html')

    
    
def log(request):
    if request.method == 'POST':
        dataa=tbl_login.objects.all()
        un=request.POST.get('username')
        pwd=request.POST.get('passwd')
        
        flag=0
            
        for da in dataa:
            if un == da.user_name and pwd == da.password:
                type=da.cat
                
                flag = 1
                if type=="admin":
                    request.session['admin']=un
                    return redirect('/adminhome/')   
                elif type=="cust":
                    request.session['cust']=un
                    return redirect('/userhome/')  
                elif type=="rest":
                    request.session['rest']=un
                    return redirect('/resthome/')  
                elif type=="emp":
                    request.session['emp']=un
                    return redirect('/employeehome/')  
                
                
                else:
                    return HttpResponse("Invalid acct type")
        if flag==0:
            return HttpResponse("Invalid user")
def viewmenu(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_menu.objects.filter(rest_id_id=request.session['rest'])
        # data=tbl_menu.objects.all()
        return render(request,"viewmenu.html",{'data1':data})

def changeprice(request,id2):
    data=tbl_menu.objects.get(menu_id=id2)
    return render(request,"changeprice.html",{'data1':data})

def changeprice1(request,id1):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_menu.objects.get(menu_id=id1)  
        data.menu_name=request.POST.get('menu_name')
        data.price=request.POST.get('price')
        data.save()

        return redirect('/viewmenu/')
def removemenuview(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        # data=tbl_menu.objects.all()
        data=tbl_menu.objects.filter(rest_id_id=request.session['rest'])
        return render(request,"viewmenu1.html",{'data1':data})

def removemenu1(request,id1):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_menu.objects.get(menu_id=id1)
        data.delete()
        return redirect('/removemenuview/')

def addtable(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.table_id
        id = int(id+1)
        table_id = "TABLE_00" + str(id)
        request.session["table_id"] = id
        return render(request,"addtable.html",{'table_id':table_id})

def addtablef(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_table()
            data.table_id=request.POST.get('table_id')
            data.table_no=request.POST.get('table_no')
            data.rest_id_id=request.session['rest']
            data.numberof_chair=request.POST.get('numberof_chair')
            data.status="Available"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.table_id=request.session['table_id']
            data1.save()
            
            return render(request,'resthome.html')

def removetableview(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        # data=tbl_table.objects.all()
        data=tbl_table.objects.filter(rest_id_id=request.session['rest'])
        return render(request,"viewtable.html",{'data1':data})

def removetable(request,id1):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_table.objects.get(table_id=id1)
        data.delete()
        return redirect('/removetableview/')

def updatetablestatusview(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        # data=tbl_table.objects.all()
        data=tbl_table.objects.filter(rest_id_id=request.session['rest'])
        return render(request,"viewtable1.html",{'data1':data})

def updatetable(request,id1):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_table.objects.get(table_id=id1)
        return render(request,"tableupdate.html",{'data':data})

def updatetable1(request,id2):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_table.objects.get(table_id=id2)  
        data.table_no=request.POST.get('table_no')
        data.numberof_chair=request.POST.get('numberof_chair')
        data.status=request.POST.get('status')
        data.save()
        return redirect('/updatetablestatusview/')


def addreview(request):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.review_id
        id = int(id+1)
        r = data1.review_id
        review_id = "REVIEW_00" + str(id)
        request.session["review_id"] = id
        request.session['r'] = review_id
        data=tbl_restaurent.objects.all()

        return render(request,"addreview.html",{'review_id':review_id,'data':data})

def addreviewf(request):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_review()
            data.review_id=request.session['r']
            data.rest_id_id=request.POST.get('name')
            s=request.session['cust']
            data1=tbl_customer.objects.get(email=s)
            data.cust_id_id=data1.cust_id
            data.review=request.POST.get('review')
            data.review_date=datetime.datetime.now().strftime ("%Y-%m-%d")
            Photo = request.FILES['photo']
            fs = FileSystemStorage()
            filename = fs.save(Photo.name, Photo) 
            uploaded_file_url = fs.url(filename)
            data.photo=uploaded_file_url
            
            data.save()
            data1=idgen.objects.get(id=1)
            data1.review_id=request.session['review_id']
            data1.save()
            
            return render(request,'custhome.html')

def viewreview(request):
    if 'admin' not in request.session:
        return render(request,"login.html")  
    else:
        data=tbl_review.objects.all()
        return render(request,"viewreview.html",{'data1':data})

def adminlogout(request):
    del request.session['admin']
    return render(request,"index.html")
def restlogout(request):
    del request.session['rest']
    return render(request,"index.html")
def custlogout(request):
    del request.session['cust']
    return render(request,"index.html")
def emplogout(request):
    del request.session['emp']
    return render(request,"index.html")
def addemployee(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.emp_id
        id = int(id+1)
        emp_id = "EMPNO_00" + str(id)
        request.session["emp_id"] = id
        return render(request,"addemployee.html",{'emp_id':emp_id})

def empregistrationf(request):
    if 'rest' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_employee()
            data.emp_id=request.POST.get('emp_id')
            data.rest_id_id=request.session['rest']
            data.name=request.POST.get('name')
            data.job="Professional"
            data.doj=request.POST.get('doj')
            data.age=request.POST.get('age')
            data.gender=request.POST.get('status')
            data.house_name=request.POST.get('house_name')
            data.street=request.POST.get('street')
            data.city=request.POST.get('city')
            data.district=request.POST.get('district')
            data.state=request.POST.get('state')
            data.pin_code=request.POST.get('pin_code')
            data.phone=request.POST.get('phone')
            data.email=request.POST.get('email')
            data.status="available"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.emp_id=request.session['emp_id']
            data1.save()
            log=tbl_login()
            log.user_name=data.email
            log.password=data.phone
            log.cat="emp"
            log.save()

        
        return render(request,'resthome.html')

def viewrestaurant(request):
    
        data=tbl_restaurent.objects.all()
        return render(request,"viewrestaurant.html",{'data1':data})
def viewrestmenu(request,id1):

    data=tbl_menu.objects.filter(rest_id_id=id1)
    return render(request,"viewrestmenu.html",{'data1':data})

def tablebooking(request,id1):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.tbl_book_id
        id = int(id+1)
        cust_id = data1.cust_id
        tbl_book_id = "TBLBNO_00" + str(id)
        request.session["tbl_book_id"] = id
        
        c=tbl_customer.objects.get(email=request.session['cust'])
        print(c)
        data=tbl_table.objects.all()
        data1=tbl_menu.objects.get(menu_id=id1)
        return render(request,"tablebooking.html",{'tbl_book_id':tbl_book_id,'c':c,'data':data,'data1':data1})

def tablebooking1(request):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_tablebooking()
            data.tbl_book_id=request.POST.get('tbl_book_id')
            data.rest_id_id=request.POST.get('rest_id')
            data.cust_id_id=request.POST.get('cust_id')
            data.table_id_id=request.POST.get('table_id')
            data.date=request.POST.get('date')
            data.time=request.POST.get('time')
            data.status="Booked"
            data.save()
            data10=tbl_table.objects.get(table_id=request.POST.get('table_id'))
            data10.status="Booked"
            data10.save()
            data1=idgen.objects.get(id=1)
            data1.tbl_book_id=request.session['tbl_book_id']
            data1.save()
            return render(request,'custhome.html')

def booktable(request):
    data=tbl_restaurent.objects.all()
    return render(request,"booktable.html",{'data1':data})

def booktable1(request,id1):
    
    data=tbl_table.objects.filter(rest_id_id=id1).filter(status="available")
    return render(request,"viewtablebook.html",{'data1':data})

def bookchair(request,id1):
    
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.tbl_book_id
        id = int(id+1)
        cust_id = data1.cust_id
        tbl_book_id = "TBLBNO_00" + str(id)
        request.session["tbl_book_id"] = id
        
        c=tbl_customer.objects.get(email=request.session['cust'])
        print(c)
        data=tbl_table.objects.all()
        data1=tbl_table.objects.get(table_id=id1)
        
        return render(request,"tablebooking.html",{'tbl_book_id':tbl_book_id,'c':c,'data':data,'data1':data1})

def placeorder(request):
    data=tbl_restaurent.objects.all()
    return render(request,"viewplaceordrestaurant.html",{'data1':data})

def viewmenuordr(request,id1):
    data=tbl_menu.objects.filter(rest_id_id=id1)
    return render(request,"viewodrmenu.html",{'data1':data})

def bookordr(request,id1):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        
        data1 = idgen.objects.get(id=1)
        id = data1.cust_orderid
        id = int(id+1)
        cust_id = data1.cust_id
        cust_orderid = "ODR_00" + str(id)
        request.session["cust_orderid"] = id
        
        
        
        data1=tbl_menu.objects.get(menu_id=id1)
        return render(request,"order.html",{'cust_orderid':cust_orderid,'data1':data1})

def bookordr1(request,id):
    if 'cust' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data1=tbl_menu.objects.get(menu_id=id)
            data=tbl_cust_order()
            data.cust_orderid=request.POST.get('cust_orderid')
            data.rest_id_id=data1.rest_id_id
            data.menu_id_id=data1.menu_id
            u=int(data1.price)
            q=int(request.POST.get('req_quantity'))
            amount=u*q
            data.req_quantity=request.POST.get('req_quantity')
            data.amount=amount
            data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
            data.status="Processing"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.cust_orderid=request.session['cust_orderid']
            data1.save()
            data1 = idgen.objects.get(id=1)
            id = data1.appl_id
            id = int(id+1)
            payment_id = "PAY_00" + str(id)
            request.session["payment_id"] = id          
            return render(request,'payment.html',{'data1':data,'payment_id':payment_id})

def payment1(request,id):
    if request.method=='POST':
            data=tbl_payment()
            
            data.payment_id=request.POST.get('payment_id')
            data.cust_orderid_id=request.POST.get('cust_orderid')
            data.payment_type=request.POST.get('type')
            data.bank=request.POST.get('bank')
            data.account=request.POST.get('Account')
            data.ifsc=request.POST.get('ifsc')
            data.amount=request.POST.get('amount')
            data.status="Pending"
            data.save()
            data=tbl_cust_order.objects.get(cust_orderid=id)
            return render(request,"viewbill.html",{'data':data})

          


def stallallotment(request):
    data=tbl_restaurent.objects.filter(status="verified")
    return render(request,"viewstallrestaurant.html",{'data1':data})

def restallot(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        
        data1 = idgen.objects.get(id=1)
        id = data1.r_s_id
        id = int(id+1)
        cust_id = data1.cust_id
        r_s_id = "ALT_00" + str(id)
        request.session["r_s_id"] = id
        
        
        
        data1=tbl_restaurent.objects.get(rest_id=id1)
        data=tbl_stall.objects.filter(status="Available")
        return render(request,"reststallallot.html",{'r_s_id':r_s_id,'data1':data1,'data':data})


def restallot1(request):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_rest_stall()
            data.r_s_id=request.POST.get('r_s_id')
            data.rest_id_id=request.POST.get('rest_id')
            data.stall_id_id=request.POST.get('stall_id')
           
            data.date=datetime.datetime.now().strftime ("%Y-%m-%d")
            data.status="Occupied"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.r_s_id=request.session['r_s_id']
            data1.save()
            data2=tbl_restaurent.objects.get(rest_id=request.POST.get('rest_id'))
            data2.status="rest allot"
            data2.save()
            data3=tbl_stall.objects.get(stall_id=request.POST.get('stall_id'))
            data3.status="Not Available"
            data3.save()
            return render(request,'adminhome.html')

def updatestallstatus(request):
     if 'admin' not in request.session:
        return render(request,"login.html")
     else:
        data=tbl_rest_stall.objects.all()
        return render(request,"viewupdatestallstatus.html",{'data1':data})

def eliminatestall(request,id1):
    if 'admin' not in request.session:
        return render(request,"login.html")
    else:
        data=tbl_rest_stall.objects.get(r_s_id=id1)
        data1=tbl_stall.objects.get(stall_id=data.stall_id_id)
        
        data.status="Not Occupied"
        data1.status="Available"
        data.save()
        data1.save()
        return render(request,'adminhome.html')

def dutyallotment(request):
    data=tbl_employee.objects.filter(rest_id_id=request.session['rest'])
    # data=tbl_employee.objects.all()
    return render(request,"viewdutyallotment.html",{'data1':data})

def allotduty(request,id1):
    data1 = idgen.objects.get(id=1)
    id = data1.emp_duty_id
    id = int(id+1)
    emp_duty_id = data1.emp_duty_id
    emp_duty_id = "ALT_00" + str(id)
    request.session["emp_duty_id"] = id
        
        
        
    data1=tbl_employee.objects.get(emp_id=id1)
    
    data=tbl_employee.objects.get(emp_id=id1)
    return render(request,"dutyallotment.html",{'data1':data,'emp_duty_id':emp_duty_id})

def dutyallotment1(request,id1):
    if request.method=='POST':
        data=tbl_employee.objects.get(emp_id=id1)
        data.job=request.POST.get('status')
        
        data.save()
        data1=tbl_emp_duty()
        data1.emp_duty_id=request.POST.get('emp_duty_id')
        data1.emp_id_id=request.POST.get('emp_id')
        data1.duty=request.POST.get('status')
        data1.allotment_date=request.POST.get('allotment_date')
        data1.status="duty Alloted"
        data1.save()
        return render(request,'resthome.html')

def dutyallotmentview(request):
    data=tbl_employee.objects.get(email=request.session['emp'])
    return render(request,"dutyallotmentview.html",{'data1':data})
    
def leaveapplication(request):
    if 'emp' not in request.session:
        return render(request,"login.html")
    else:
        data1 = idgen.objects.get(id=1)
        id = data1.appl_id
        id = int(id+1)
        appl_id = "LAPP_00" + str(id)
        request.session["appl_id"] = id
        data1=tbl_employee.objects.get(email=request.session['emp'])
        return render(request,"leaveapplication.html",{'appl_id':appl_id,'data1':data1})

def leaveapplicationf(request):
    if 'emp' not in request.session:
        return render(request,"login.html")
    else:
        if request.method=='POST':
            data=tbl_leave_application()
            data.appl_id=request.POST.get('appl_id')
            data.rest_id_id=request.POST.get('rest_id')
            data.emp_id_id=request.POST.get('emp_id')
            data.leave_appl_date=datetime.datetime.now().strftime ("%Y-%m-%d")
            data.leave_date=request.POST.get('leave_date')
            data.no_of_days=request.POST.get('no_of_days')
            data.remark=request.POST.get('remark')
            
            data.status="Pending"
            data.save()
            data1=idgen.objects.get(id=1)
            data1.appl_id=request.session['appl_id']
            data1.save()
            return render(request,'employeehome.html')

def leaveprocess(request):
    data=tbl_leave_application.objects.filter(rest_id_id=request.session['rest'])
    return render(request,"leaveprocess.html",{'data1':data})

def approveleave(request,id1):
    data=tbl_leave_application.objects.get(appl_id=id1)
    return render(request,"approveleave.html",{'data':data})

def approveleave1(request,id1):
    data=tbl_leave_application.objects.get(appl_id=id1)
    data.status="Approved"
    data.save()
    return redirect('/leaveprocess/')

def rejectleave(request,id2):
    data=tbl_leave_application.objects.get(appl_id=id2)
    data.status="Rejected"
    data.save()
    return redirect('/leaveprocess/')

def viewleaveapplicationstatus(request):
    data1=tbl_employee.objects.get(email=request.session['emp'])
    data3=data1.emp_id
    data=tbl_leave_application.objects.filter(emp_id_id=data3)
    return render(request,"viewleaveapplicationstatus.html",{'data1':data})
def pay(request,id2):
    data=tbl_cust_order.objects.get(cust_orderid=id2)
    return render(request,"viewbill.html",{'data':data})

def vieworder(request):
    data=tbl_cust_order.objects.filter(rest_id_id=request.session['rest'])
    return render(request,"vieworder.html",{'data1':data})

def orderclose(request,id1):
    data=tbl_cust_order.objects.get(cust_orderid=id1)
    data.status="order accept"
    data.save()
    return render(request,"viewbill2.html",{'data':data})

def tablebookingmanage(request):
    data=tbl_tablebooking.objects.filter(rest_id_id=request.session['rest'])
    
    data=tbl_table.objects.filter(status="Booked")
    return render(request,"tablebookingmanage.html",{'data1':data})

def Makeavailable(request,id1):
    data=tbl_table.objects.get(table_id=id1)
    data.status="Available"
    data.save()
    
    return redirect('/tablebookingmanage/')

def publicreview(request):
    data=tbl_review.objects.all()
    return render(request,"viewreviewpublic.html",{'data1':data})

def custreview(request):
    data=tbl_review.objects.all()
    return render(request,"custreview.html",{'data1':data})

def adminhome(request):
    return render(request,"adminhome.html")

def report(request):
    data=tbl_stall.objects.all()
    data1=tbl_rest_stall.objects.all()
    data2=tbl_restaurent.objects.all()
    
    return render(request,"report.html",{'data1':data,'data2':data1})
   

def userhome(request):
    return render(request,"custhome.html")

def restreport(request):
    return render(request,"restreport.html")
    
def reportadmin(request):
    data=tbl_restaurent.objects.all()
    return render(request,"reportadmin.html",{'data1':data})

def searadmin(request):
    if request.method=='POST':
        q=request.POST.get('name')
        data1=tbl_restaurent.objects.filter(rest_id=q)
        data=tbl_rest_stall.objects.filter(rest_id_id=q)
        
        return render(request,"searchadmin.html",{'data':data1,'data2':data,'q1':q})

def publicviewrest(request):
    
        data=tbl_restaurent.objects.all()
        return render(request,"publicviewrest.html",{'data1':data})

def viewmenuordrpublic(request,id1):
    data=tbl_menu.objects.filter(rest_id_id=id1)
    return render(request,"viewmenuordrpublic.html",{'data1':data})


















    






        

    



        

        
    



















  



