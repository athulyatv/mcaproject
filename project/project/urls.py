"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.home),
    path('login/',views.loginf),
    path('registration/',views.regf),
    path('forms/',views.forms),
    path('menubar/',views.menubarf),
    path('admin_menubar/',views.admin_menubarf),
    path('addstall/',views.addstall),
    path('addstallf/',views.addstallf),
    path('removestall/',views.removestall),
    path('removestall1/<str:id1>',views.removestall1),
    path('updatestall/<str:id1>',views.updatestall),
    path('updatestall2/<str:id2>',views.updatestall2),
    path('customerregistration/',views.customerregistration),
    path('customerregistrationf/',views.customerregistrationf),
    path('res/',views.restaurentregistration),
    path('restaurentregistrationf/',views.restaurentregistrationf),
    path('restappscn/',views.restappscn),
    path('verifyrest1/<str:id1>',views.verifyrest1),
    path('accept/<str:id1>',views.accept),
    path('reject/<str:id1>',views.reject),
    path('rest_menubar/',views.rest_menubarf),
    path('addmenu/',views.addmenu),
    path('addmenuf/',views.addmenuf),
    path('login/',views.loginf),
    path('adminhome/',views.adminhome),
    path('userhome/',views.userhome),
    path('resthome/',views.resthome),
    path('employeehome/',views.employeehome),
    path('log/',views.log),
    path('viewmenu/',views.viewmenu),
    path('changeprice/<str:id2>',views.changeprice),
    path('changeprice1/<str:id1>',views.changeprice1),
    path('removemenuview/',views.removemenuview),
    path('removemenu1/<str:id1>',views.removemenu1),
    path('addtable/',views.addtable),
    path('addtablef/',views.addtablef),
    path('removetableview/',views.removetableview),
    path('removetable/<str:id1>',views.removetable),
    path('updatetablestatusview/',views.updatetablestatusview),
    path('updatetable/<str:id1>',views.updatetable),
    path('updatetable1/<str:id2>',views.updatetable1),
    path('cust_menubar/',views.cust_menubar),
    path('addreview/',views.addreview),
    path('addreviewf/',views.addreviewf),
    path('viewreview/',views.viewreview),
    path('adminlogout/',views.adminlogout),
    path('restlogout/',views.restlogout),
    path('custlogout/',views.custlogout),
    path('addemployee/',views.addemployee),
    path('empregistrationf/',views.empregistrationf),
    path('emplogout/',views.emplogout),
    path('viewrestaurant/',views.viewrestaurant),
    path('viewrestmenu/<str:id1>',views.viewrestmenu),
    path('tablebooking/<str:id1>',views.tablebooking),
    path('tablebooking1/',views.tablebooking1),
    path('booktable/',views.booktable),
    path('booktable1/<str:id1>',views.booktable1),
    path('bookchair/<str:id1>',views.bookchair),
    path('placeorder/',views.placeorder),
    path('viewmenuordr/<str:id1>',views.viewmenuordr),
    path('bookordr/<str:id1>',views.bookordr),
    path('bookordr1/<str:id>',views.bookordr1),
    path('payment1/<str:id>',views.payment1),
    path('stallallotment/',views.stallallotment),
    path('restallot/<str:id1>',views.restallot),
    path('restallot1/',views.restallot1),
    path('updatestallstatus/',views.updatestallstatus),
    path('eliminatestall/<str:id1>',views.eliminatestall),
    path('dutyallotment/',views.dutyallotment),
    path('allotduty/<str:id1>',views.allotduty),
    path('dutyallotment1/<str:id1>',views.dutyallotment1),
    path('dutyallotmentview/',views.dutyallotmentview),
    path('leaveapplication/',views.leaveapplication),
    path('leaveapplicationf/',views.leaveapplicationf),
    path('leaveprocess/',views.leaveprocess),
    path('approveleave/<str:id1>',views.approveleave),
    path('approveleave1/<str:id1>',views.approveleave1),
    path('rejectleave/<str:id2>',views.rejectleave),
    path('viewleaveapplicationstatus/',views.viewleaveapplicationstatus),
    path('pay<str:id2>',views.pay),
    path('vieworder/',views.vieworder),
    path('orderclose/<str:id1>',views.orderclose),
    path('tablebookingmanage/',views.tablebookingmanage),
    path('Makeavailable/<str:id1>',views.Makeavailable),
    path('publicreview/',views.publicreview),
    path('custreview/',views.custreview),
    path('adminhome/',views.adminhome),
    path('report/',views.report),
    path('userhome/',views.userhome),
    path('restreport/',views.restreport),
    path('reportadmin/',views.reportadmin),
    path('searadmin/',views.searadmin),
    path('publicviewrest/',views.publicviewrest),
    path('viewmenuordrpublic/<str:id1>',views.viewmenuordrpublic),



    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)