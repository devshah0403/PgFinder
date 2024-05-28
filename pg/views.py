from django.contrib import messages
from django.shortcuts import render,redirect
from django.utils.dateparse import parse_date
from pg import function
from pg.forms import *
from pg.function import handle_uploaded_file
from pg.models import USER_TABLE,OWNER_TABLE,PG_DETAILS,BOOKING,CATEGORY_TABLE,AREA
import sys

from pgfinder import settings


# Create your views here.
def index(request):
    return render(request,"data.html")

def showUser(request):
    if 'admin_id' in request.session:
        u = USER_TABLE.objects.all()
        return render(request,"user-show.html",{'user_table':u})
    else:
        return redirect('/404/')
def error(request):
    return render(request,"404.html")
def destroyUser(request,id):
    if 'admin_id' in request.session:
        e=USER_TABLE.objects.get(user_id=id)
        e.delete()
        return redirect("/usershow")
    else:
        return redirect('/404/')
def showOwner(request):
    if 'admin_id' in request.session:
        u = OWNER_TABLE.objects.all()
        return render(request,"owner-show.html",{'owner_table':u})
    else:
        return redirect('/404/')
def dashboard(request):
    if 'admin_id' in request.session:
        u=USER_TABLE.objects.all().count()
        p=PG_DETAILS.objects.all().count()
        o=OWNER_TABLE.objects.all().count()
        b=BOOKING.objects.all().count()
        return render(request,"dashboard.html",{"user":u,"pg":p,"owner":o,"book":b})
    else:
        return redirect('/404/')

def insertUser(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            form=UserForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/usershow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=UserForm()
        return render(request,"user-insert.html",{"form":form})
    else:
        return redirect('/404/')
def selectUser(request,id):
    if 'admin_id' in request.session:
        u_data=USER_TABLE.objects.get(user_id=id)
        return render(request, "user-edit.html", {'user_table': u_data})
    else:
        return redirect('/404/')
def updateUser(request,id):
    if 'admin_id' in request.session:
        u_data=USER_TABLE.objects.get(user_id=id)
        form=UserForm(request.POST,instance=u_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/usershow')
            except:
                print("------------",sys.exc_info())
        return render(request,"user-edit.html",{'user_table':u_data})
    else:
        return redirect('/404/')
#===================================OWNER=================================================
def insertOwner(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            form=OwnerForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/ownershow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=OwnerForm()
        return render(request,"owner-insert.html",{"form":form})
    else:
        return redirect('/404/')
def destroyOwner(request,id):
    if 'admin_id' in request.session:
        e=OWNER_TABLE.objects.get(o_id=id)
        e.delete()
        return redirect("/ownershow")
    else:
        return redirect('/404/')
def selectOwner(request,id):
    if 'admin_id' in request.session:
        o_data=OWNER_TABLE.objects.get(o_id=id)
        return render(request, "owner-edit.html", {'owner_table': o_data})
    else:
        return redirect('/404/')
def updateOwner(request,id):
    if 'admin_id' in request.session:
        o_data=OWNER_TABLE.objects.get(o_id=id)
        form=OwnerForm(request.POST,instance=o_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/ownershow')
            except:
                print("------------",sys.exc_info())
        return render(request,"owner-edit.html",{'owner_table':o_data})
    else:
        return redirect('/404/')
#====================================CATEGORY======================================
def showCat(request):
    if 'admin_id' in request.session:
        u = CATEGORY_TABLE.objects.all()
        return render(request,"cat-show.html",{'cat_table':u})
    else:
        return redirect('/404/')
def destroyCat(request,id):
    if 'admin_id' in request.session:
        e=CATEGORY_TABLE.objects.get(c_id=id)
        e.delete()
        return redirect("/catshow")
    else:
        return redirect('/404/')
def insertCat(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            form=CategoryForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/catshow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=CategoryForm()
        return render(request,"cat-insert.html",{"form":form})
    else:
        return redirect('/404/')
def selectCat(request,id):
    if 'admin_id' in request.session:
        c_data=CATEGORY_TABLE.objects.get(c_id=id)
        return render(request, "cat-edit.html", {'cat_table': c_data})
    else:
        return redirect('/404/')
def updateCat(request,id):
    if 'admin_id' in request.session:
        c_data=CATEGORY_TABLE.objects.get(c_id=id)
        form=CategoryForm(request.POST,instance=c_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/catshow')
            except:
                print("------------",sys.exc_info())
        return render(request,"cat-edit.html",{'cat_table':c_data})
    else:
        return redirect('/404/')
#===================================PG=============================================
def showPg(request):
    if 'admin_id' in request.session:
        p=PG_DETAILS.objects.all()
        return render(request,"pg-show.html",{'pg_details':p})
    else:
        return redirect('/404/')

def insertPg(request):
    if 'admin_id' in request.session:
        cat = CATEGORY_TABLE.objects.all()
        o = OWNER_TABLE.objects.all()
        obj = AREA.objects.all()
        if request.method=="POST":
            form=PGdetialsForm(request.POST,request.FILES)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    handle_uploaded_file(request.FILES["pg_img"])
                    form.save()
                    return redirect("/pgshow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=PGdetialsForm()
        return render(request,"pg-insert.html",{"form":form,'cat_table':cat,'owner_table':o,"area":obj})
    else:
        return redirect('/404/')
def destroyPg(request,id):
    if 'admin_id' in request.session:
        e=PG_DETAILS.objects.get(pg_id=id)
        e.delete()
        return redirect("/pgshow")
    else:
        return redirect('/404/')
def updatePg(request,id):
    if 'admin_id' in request.session:
        cat=CATEGORY_TABLE.objects.all()
        o=OWNER_TABLE.objects.all()
        c_data=PG_DETAILS.objects.get(pg_id=id)
        obj=AREA.objects.all()
        form=PGdetialsForm(request.POST,instance=c_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/pgshow')
            except:
                print("------------",sys.exc_info())
        return render(request,"pg-edit.html",{'pg_table':c_data,'cat_table':cat,'owner_table':o,"area":obj})
    else:
        return redirect('/404/')
def selectPg(request,id):
    if 'admin_id' in request.session:
        c_data=PG_DETAILS.objects.get(pg_id=id)
        return render(request, "pg-edit.html", {'pg_table': c_data})
    else:
        return redirect('/404/')
#==================================BOOKING===========================================
def showBook(request):
    if 'admin_id' in request.session:
        obj=BOOKING.objects.all()
        return render(request,'book-show.html',{'form':obj})
    else:
        return redirect('/404/')



#==================================GRAPH===========================================
from django.db import connection
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

#from company.models import Company


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request,'dashboard.html', {"customers": 10})




class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):


        #qs = Company.objects.all()


        cursor=connection.cursor()
        cursor.execute('''select b_id,b_amt from book_table''')
        qs=cursor.fetchall()



        labels = []
        default_items = []

        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])

        data = {
            "labels": labels,
            "default": default_items,
        }

        return Response(data)

def profile(request):
    if 'admin_id' in request.session:
        return render(request,"profile.html")

#==============================LOGIN===========================================================

from django.core.mail import send_mail
import random


def sendotp(request):

    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail']=e

    obj = USER_TABLE.objects.filter(user_email=e).count()

    if obj == 1:

        val = USER_TABLE.objects.filter(user_email=e).update(otp=otp1 , otp_used=0)

        subject = 'OTP Verification for PG-Finder'
        message = 'One-Time Password for PG-Finder :'+str(otp1)+'<br> Donot share it with anyone.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'set_password.html')
    else:
        messages.error(request, "Invalid Email.")
        return render(request, "forgot.html")


def forgot(request):
    return render(request,"forgot.html")

def set_password(request):

    if request.method == "POST":

        T_otp = request.POST['otp']
        T_pass = request.POST['pass']
        T_cpass = request.POST['cpass']

        if T_pass == T_cpass:

            e = request.session['temail']
            val = USER_TABLE.objects.filter(user_email=e,otp = T_otp,otp_used = 0).count()

            if val == 1:
                USER_TABLE.objects.filter(user_email = e).update(otp_used = 1,user_pass = T_pass)
                return redirect("/login")
            else:
                messages.error(request,"Invalid OTP")
                return render(request,"forgot.html")

        else:
            messages.error(request,"New password and Confirm password does not match ")
            return render(request,"set_password.html")

    else:
        return redirect("/forgot_password")

def adminLogout(request):
    if 'admin_id' in request.session:
        try:
            del request.session['admin_id']
            del request.session['admin_fname']
            del request.session['admin_lname']
            del request.session['admin_email']
        except:
            pass
        return redirect('/login')
    else:
        return redirect('/404/')
def adminLogin(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["pass"]
        val=USER_TABLE.objects.filter(user_email=email,user_pass=password,is_admin=1).count()
        if val==1:
            data = USER_TABLE.objects.filter(user_email=email, user_pass=password, is_admin=1)
            for i in data:
                request.session['admin_id']=i.user_id
                request.session['admin_fname'] = i.user_fname
                request.session['admin_lname'] = i.user_lname
                request.session['admin_email'] = i.user_email
            if request.POST.get("rem"):
                response=redirect("/dashboard/")
                response.set_cookie('c_aemail',request.POST["email"], 3600 * 24 * 365 * 2)
                response.set_cookie('c_apass', request.POST["pass"], 3600 * 24 * 365 * 2)
                return response
            return redirect("/dashboard/")
        else:
            messages.error(request,"Invalid Username and Password")
            return redirect("/login/")

    else:
        if request.COOKIES.get('c_aemail'):
            return render(request,"auth-login.html",{'a_email_cookie':request.COOKIES['c_aemail'],'a_pass_cookie':request.COOKIES['c_apass']})
        else:
            return render(request,"auth-login.html")



    return redirect("/login")

def show1(request):
    return render(request,"data.html")

#===================================REPORT===============================================

def report_1(request):
    if 'admin_id' in request.session:
        sql="SELECT 1 as b_id,p.pg_name as Name,SUM(b_amt) as Total FROM `book_table` b JOIN pg_details p WHERE p.pg_id=b.pg_id_id GROUP BY pg_id_id;"
        obj=BOOKING.objects.raw(sql)
        return render(request,'report-1.html',{'form':obj})
    else:
        return redirect('/404/')
def report_2(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            s_d=request.POST['start']
            e_d=request.POST['end']
            start=parse_date(s_d)
            end=parse_date(e_d)
            obj=BOOKING.objects.filter(b_date__range=[start,end])
        else:
            obj=BOOKING.objects.all()
        return render(request,'report-2.html',{'form':obj})
    else:
        return redirect('/404/')
def report_3(request):
    if 'admin_id' in request.session:
        obj=AREA.objects.all()
        if request.method=="POST":
            val=request.POST['area']
            val1=PG_DETAILS.objects.filter(area_id_id=val)
        else:
            val1=PG_DETAILS.objects.all()
        return render(request,'report-3.html',{'area':obj,'loc':val1})
    else:
        return redirect('/404/')
#=======================================AREA=======================================
def showArea(request):
    if 'admin_id' in request.session:
        a=AREA.objects.all()
        return render(request,"area-show.html",{'area_table':a})
    else:
        return redirect('/404/')
def insertArea(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            form=AreaForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/areashow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=AreaForm()
        return render(request,"area-insert.html",{"form":form})
    else:
        return redirect('/404/')
def destroyArea(request,id):
    if 'admin_id' in request.session:
        a=AREA.objects.get(area_id=id)
        a.delete()
        return redirect("/areashow")
    else:
        return redirect('/404/')
def updateArea(request,id):
    if 'admin_id' in request.session:
        a_data=AREA.objects.get(area_id=id)
        form=AreaForm(request.POST,instance=a_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/areashow')
            except:
                print("------------",sys.exc_info())
        return render(request,"area-edit.html",{'area_table':a_data})
    else:
        return redirect('/404/')
#==========================================FACILITY====================================
def showFacility(request):
    if 'admin_id' in request.session:
        f=FACILITY.objects.all()
        return render(request,"facility-show.html",{'facility_table':f})
    else:
        return redirect('/404/')
def insertFacility(request):
    if 'admin_id' in request.session:
        if request.method=="POST":
            form=FacilityForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/facilityshow")
                except:
                    print("----------",sys.exc_info())
        else:
            form=FacilityForm()
        return render(request,"facility-insert.html",{"form":form})
    else:
        return redirect('/404/')
def updateFacility(request,id):
    if 'admin_id' in request.session:
        f_data=FACILITY.objects.get(f_id=id)
        form=FacilityForm(request.POST,instance=f_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/facilityshow')
            except:
                print("------------",sys.exc_info())
        return render(request,"facility-edit.html",{'facility_table':f_data})
    else:
        return redirect('/404/')
def destroyFacility(request,id):
    if 'admin_id' in request.session:
        f=FACILITY.objects.get(f_id=id)
        f.delete()
        return redirect("/facilityshow")
    else:
        return redirect('/404/')
#============================================FEEDBACK===========================================
def showFeed(request):
    if 'admin_id' in request.session:
        f=FEEDBACK_TABLE.objects.all()
        return render(request,"feedback-show.html",{'feed_table':f})
    else:
        return redirect('/404/')
def destroyFeed(request,id):
    if 'admin_id' in request.session:
        f=FEEDBACK_TABLE.objects.get(f_id=id)
        f.delete()
        return redirect("/feedshow")
    else:
        return redirect('/404/')
#==========================================PG FACILITY===============================================
def showPgfacility(request):
    if 'admin_id' in request.session:
        pf=PG_FACILITY.objects.all()
        return render(request,"pgfacility-show.html",{'pgfacility_table':pf})
    else:
        return redirect('/404/')



#============================
def showimgedit(request,id):
    obj=PG_DETAILS.objects.get(pg_id=id)
    return render(request,"pgimgedit.html",{'pg_table':obj})

def updimg(request,id):
    if request.method == "POST":
        img=request.FILES["pg_img"]
        handle_uploaded_file(request.FILES['pg_img'])
        obj=PG_DETAILS.objects.filter(pg_id=id).update(pg_img=img)
        return redirect("/pgshow/")

def featured(request,id):
    if 'o_id' in request.session:

        o = PG_DETAILS.objects.get(pg_id=id)
        o.is_featured = '1'
        o.save()

def not_featured(request,id):
    if 'o_id' in request.session:

        o = PG_DETAILS.objects.get(pg_id=id)
        o.is_featured = '0'
        o.save()