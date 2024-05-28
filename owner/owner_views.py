import sys
from datetime import date

from django.core.mail import send_mail
from django.shortcuts import render, redirect

from pg.forms import *
from pg.function import handle_uploaded_file
from pg.models import *
from pgfinder import settings


# Create your views here.
def error(request):
    return render(request,"o_404.html")



def show(request):
    if 'o_id' in request.session:
        id=request.session['o_id']
        obj=OWNER_TABLE.objects.get(o_id=id)
        return render(request,'index.html',{'form':obj})
    else:
        return redirect('/owner/error/')

def areashow(request):
    if 'o_id' in request.session:
        a=AREA.objects.all()
        return render(request,"areashow.html",{'area_table':a})
    else:
        return redirect('/owner/error/')

def facilityshow(request):
    if 'o_id' in request.session:
        f=FACILITY.objects.all()
        return render(request,"facilityshow.html",{'facility_table':f})
    else:
        return redirect('/owner/error/')

def insertFacility(request):
    if 'o_id' in request.session:

        if request.method=="POST":
            form=FacilityForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/owner/facility')
                except:
                    print("----------",sys.exc_info())
        else:
            form=FacilityForm()
        return render(request,"facilityinsert.html",{"form":form})
    else:
        return redirect('/owner/error/')
def updateFacility(request,id):
    if 'o_id' in request.session:

        f_data=FACILITY.objects.get(f_id=id)
        form=FacilityForm(request.POST,instance=f_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/owner/facility')
            except:
                print("------------",sys.exc_info())
        return render(request,"facilityedit.html",{'facility_table':f_data})
    else:
        return redirect('/owner/error/')
def destroyFacility(request,id):
    if 'o_id' in request.session:

        f=FACILITY.objects.get(f_id=id)
        f.delete()
        return redirect("/owner/facility")
    else:
        return redirect('/owner/error/')


def usershow(request,id):
    if 'o_id' in request.session:

        oid = request.session['o_id']
        u = USER_TABLE.objects.filter(user_id=id)
        obj = OWNER_TABLE.objects.get(o_id=oid)
        return render(request,"usershow.html",{'user_table':u,'form':obj})
    else:
        return redirect('/owner/error/')
def ownershow(request):
    if 'o_id' in request.session:

        id = request.session['o_id']
        u = OWNER_TABLE.objects.all()
        obj = OWNER_TABLE.objects.get(o_id=id)
        return render(request,"ownershow.html",{'owner_table':u,'form':obj})
    else:
        return redirect('/owner/error/')
def showFeed(request,id):
    if 'o_id' in request.session:

        f=FEEDBACK_TABLE.objects.filter(pg_id_id=id)
        return render(request,"feedbackshow.html",{'feed_table':f})
    else:
        return redirect('/owner/error/')

def showWishlist(request):
    if 'o_id' in request.session:

        w = WISHLIST.objects.all()
        return render(request,"wishlistshow.html",{'wishlist_table':w})
    else:
        return redirect('/owner/error/')


def destroyFeed(request,id):
    if 'o_id' in request.session:

        f=FEEDBACK_TABLE.objects.get(f_id=id)
        f.delete()
        return redirect("/owner/pg/")
    else:
        return redirect(('/owner/error/'))
def showPgfacility(request):
    if 'o_id' in request.session:

        id=request.session["o_id"]
        sql="SELECT * FROM `pgfac_table` p JOIN pg_details b JOIN fac_table f where p.pg_id_id = b.pg_id and b.o_id_id = %s;" %id
        pf=PG_DETAILS.objects.raw(sql)
        return render(request,"pgfacilityshow.html",{'pgfacility_table':pf})
    else:
        return redirect('/owner/error/')
def catshow(request):
    if 'o_id' in request.session:

        id = request.session['o_id']
        u = CATEGORY_TABLE.objects.all()
        obj = OWNER_TABLE.objects.get(o_id=id)
        return render(request,"catshow.html",{'cat_table':u,'form':obj})
    else:
        return redirect('/owner/error/')
def updateCat(request,id):
    if 'o_id' in request.session:

        c_data=CATEGORY_TABLE.objects.get(c_id=id)
        form=CategoryForm(request.POST,instance=c_data)
        print("+++++++++++++++++",form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/owner/cat')
            except:
                print("------------",sys.exc_info())
        return render(request,"catedit.html",{'cat_table':c_data})
    else:
        return redirect('/owner/error/')

def insertCat(request):
    if 'o_id' in request.session:

        if request.method=="POST":
            form=CategoryForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/owner/cat')
                except:
                    print("----------",sys.exc_info())
        else:
            form=CategoryForm()
        return render(request,"catinsert.html",{"form":form})
    else:
        return redirect('/owner/error/')


def destroyCat(request,id):
    if 'o_id' in request.session:

        e=CATEGORY_TABLE.objects.get(c_id=id)
        e.delete()
        return redirect("/owner/cat")
    else:
        return redirect('/owner/error/')

def pgshow(request):
    if 'o_id' in request.session:
        id=request.session['o_id']
        p=PG_DETAILS.objects.filter(o_id=id)
        obj = OWNER_TABLE.objects.get(o_id=id)
        return render(request,"pgshow.html",{'pg_details':p,'form':obj})
    else:
        return redirect('/owner/error/')
def insertPg(request):
    if 'o_id' in request.session:

        if request.method=="POST":
            form=PGdetialsForm(request.POST)
            print("-------------",form.errors)
            if form.is_valid():
                try:
                    form.save()
                    return redirect("/owner/pg")
                except:
                    print("----------",sys.exc_info())
        else:
            form=PGdetialsForm()
        return render(request,"pginsert.html",{"form":form})

    else:
        return redirect('/owner/error/')


def destroyPg(request,id):
    if 'o_id' in request.session:

        e=PG_DETAILS.objects.get(pg_id=id)
        e.delete()
        return redirect("/owner/pg")
    else:
        return redirect('/owner/error/')

def updatePg(request,id):
    if 'o_id' in request.session:

        cat=CATEGORY_TABLE.objects.all()

        c_data=PG_DETAILS.objects.get(pg_id=id)
        obj = AREA.objects.all()
        form=PGdetialsForm(request.POST,instance=c_data)
        print("+++++++++++++++++",form.errors)
        if request.method == "POST":
            try:
                name=request.POST["pg_name"]
                mail=request.POST["pg_email"]
                con=request.POST["pg_con"]
                add=request.POST["pg_add"]

                avail=request.POST["pg_avail"]
                price=request.POST["pg_price"]
                cat=request.POST["c_id"]
                a=request.POST["area_id"]

                p=PG_DETAILS.objects.filter(pg_id=id).update(pg_name=name,pg_email=mail,pg_con=con,pg_add=add,pg_avail=avail,pg_price=price,c_id=cat,area_id=a)
                return redirect('/owner/pg')
            except:
                print("------------",sys.exc_info())
        return render(request,"pgedit.html",{'pg_table':c_data,'cat_table':cat,"area":obj})
    else:
        return redirect('/owner/error/')


def bookshow(request):
    if 'o_id' in request.session:

        id=request.session['o_id']
        print("************woner id",id)
        sql="SELECT * FROM book_table b join pg_details p join user_table u where b.user_id_id = u.user_id and b.pg_id_id = p.pg_id and p.o_id_id =  %s;" % id
        obj1 = PG_DETAILS.objects.raw(sql)
        print("****************sql",sql)
        for data in obj1:
            print("------------------------------------",data)

        return render(request,'bookshow.html',{'data':obj1})
    else:
        return redirect('/owner/error/')
def o_profile(request):
    if 'o_id' in request.session:

        id = request.session['o_id']
        obj=OWNER_TABLE.objects.get(o_id=id)
        return render(request,'owner-profile.html',{'form':obj})
    else:
        return redirect('/owner/error/')
def ownerLogout(request):
    try:
        del request.session['o_id']
        del request.session['o_fname']
        del request.session['o_lname']
        del request.session['o_email']
    except:
        pass
    return redirect('/client/ownerlogin/')

def accept_order(request, id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.b_status = '1'
        o.save()
        e = o.user_id.user_email
        # print("--------------------------------", e)
        # subject = 'Order Status'
        # message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have accept your order, Order will reach you soon.' \
        #           f'your order id is {o.b_id}'
        #
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [e, ]
        # send_mail(subject, message, email_from, recipient_list)
        return redirect('/owner/book/')
    else:
        return redirect('/owner/error/')
def reject_order(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.b_status = '2'
        o.pay_status='2'
        o.pay_type='2'
        o.save()
        #if o.pay_status == 1:
            #e = o.user_id.user_email
           # print("--------------------------------", e)
            #subject = 'Order Status'
            #message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have regret to inform you, your order has been rejected  due to some technical issue.'

            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = [e, ]
            #send_mail(subject, message, email_from, recipient_list)
            #else:
            #e = o.user_id.user_email
            #print("--------------------------------", e)
            #subject = 'Order Status'
            #message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have regret to inform you, your order has been rejected  due to some technical issue. ' \
                    #  f'We will refund your amount in 2/3 days '


            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = [e, ]
            #send_mail(subject, message, email_from, recipient_list)
        return redirect('/owner/book/')
    else:
        return redirect('/owner/error/')
def accept_avail(request, id):
    if 'o_id' in request.session:

        o = PG_DETAILS.objects.get(pg_id=id)
        o.pg_avail = '1'
        o.save()
        return redirect('/owner/pg/')
    else:
        return redirect('/owner/error/')


def reject_avail(request,id):
    if 'o_id' in request.session:

        o=PG_DETAILS.objects.get(pg_id=id)
        o.pg_avail='2'
        o.save()
        return redirect('/owner/pg/')
    else:
        return redirect('/owner/error/')
#==========================================GRAPH===============================================
def o_dashboard(request):
    if 'o_id' in request.session :
        oid=request.session['o_id']
        print("55555555555555555555555555555555555",oid)
        sql2="SELECT 1 as f_id,COUNT(*) as total2 FROM `feed_table` f JOIN pg_details p where f.pg_id_id = p.pg_id and p.o_id_id =  %s;" %oid
        f=FEEDBACK_TABLE.objects.raw(sql2)
        for x in f:
            ft = x.total2
        p=PG_DETAILS.objects.filter(o_id_id=oid).count()
        print("00000000000000000000000000000000000000", p)
        #if p >= 1:

         #   p1=BOOKING.objects.filter(pg_id_id=p).count()
          #  print("-------------------------------------------",p1)
           # o = WISHLIST.objects.all().count()
           # return render(request,"o_dashboard.html",{"user":u,"pg":p,"wish":o,"book":p1})

        sql = "SELECT 1 as pg_id, COUNT(*) as total FROM book_table b join pg_details p where b.pg_id_id = p.pg_id and p.o_id_id = %s;" % oid
        obj1 = PG_DETAILS.objects.raw(sql)
        c=0
        for x in obj1:
            c = x.total
        print("---------------",obj1)
        # sql = "SELECT * FROM book_table;"
        # return render(request,"o_dashboard.html",{"user":u,"pg1":p,"wish":o,"book":obj1})
        d=date.today()
        print("date--------------",d)
        obj=BOOKING.objects.filter(b_date=d)
        sql1 = "select 1 as b_id, SUM(b_amt) as total1 FROM `book_table` b JOIN pg_details p where b.pg_id_id = p.pg_id and p.o_id_id = %s;" % oid
        amt=BOOKING.objects.raw(sql1)
        for x in amt:
            t=x.total1
        return render(request, "o_dashboard.html", {"user": ft, "pg": p,"rec":obj,"book":c,"total":t})
    else:
        return redirect("/client/ownerlogin/")
from django.db import connection
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

#from company.models import Company


class HomeView(View):

    def get(self, request, *args, **kwargs):
        print("********************")
        return render(request,'o_dashboard.html', {"customers": 10})




class ChartData(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        print("*********id")
        oid = request.session['o_id']
        print("*********id",oid)
        #qs = Company.objects.all()


        cursor=connection.cursor()
        cursor.execute('''SELECT * FROM book_table b join pg_details p where b.pg_id_id = p.pg_id and p.o_id_id = %s;"''' %oid)
        qs=cursor.fetchall()



        labels = []
        default_items = []

        for item in qs:
            labels.append(item[0])
            default_items.append(item[1])
            print("*****************items",item)

        data = {
            "labels": labels,
            "default": default_items,
        }

        return Response(data)







def acc_pay(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.pay_status = '1'
        o.save()
        return redirect('/owner/book/')
    else:
        return redirect('/owner/error/')


def rej_pay(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.pay_status = '2'
        o.save()
        return redirect('/owner/book/')
    else:
        return redirect('/owner/error/')

def d_accept_order(request, id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.b_status = '1'
        o.save()
        e = o.user_id.user_email
        # print("--------------------------------", e)
        # subject = 'Order Status'
        # message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have accept your order, Order will reach you soon.' \
        #           f'your order id is {o.b_id}'
        #
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = [e, ]
        # send_mail(subject, message, email_from, recipient_list)
        return redirect('/owner/o_dashboard/')
    else:
        return redirect('/owner/error/')


def d_reject_order(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.b_status = '2'
        o.pay_status='2'
        o.pay_type='2'
        o.save()
        #if o.pay_status == 1:
            #e = o.user_id.user_email
            #print("--------------------------------", e)
            #subject = 'Order Status'
            #message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have regret to inform you, your order has been rejected  due to some technical issue.'

            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = [e, ]
            #send_mail(subject, message, email_from, recipient_list)
            #else:
            #e = o.user_id.user_email
            #print("--------------------------------", e)
            #subject = 'Order Status'
            #message = f'Dear {o.user_id.user_fname} {o.user_id.user_lname}, We have regret to inform you, your order has been rejected  due to some technical issue. ' \
                    #  f'We will refund your amount in 2/3 days '


            #email_from = settings.EMAIL_HOST_USER
            #recipient_list = [e, ]
            #send_mail(subject, message, email_from, recipient_list)
        return redirect('/owner/o_dashboard/')
    else:
        return redirect('/owner/error/')


def d_acc_pay(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.pay_status = '1'
        o.save()
        return redirect('/owner/o_dashboard/')
    else:
        return redirect('/owner/error/')


def d_rej_pay(request,id):
    if 'o_id' in request.session:

        o = BOOKING.objects.get(b_id=id)
        o.pay_status = '2'
        o.save()
        return redirect('/owner/o_dashboard/')
    else:
        return redirect('/owner/error/')

######################
def showimgedit(request,id):
    if 'o_id' in request.session:

        obj=PG_DETAILS.objects.get(pg_id=id)
        return render(request,"pg_imgedit.html",{'pg_table':obj})
    else:
        return redirect('/owner/error/')



def updimg(request,id):
    if 'o_id' in request.session:

        if request.method == "POST":
            img=request.FILES["pg_img"]
            handle_uploaded_file(request.FILES['pg_img'])
            obj=PG_DETAILS.objects.filter(pg_id=id).update(pg_img=img)
            return redirect("/owner/pg/")
    else:
        return redirect('/owner/error/')


def enquiry_show(request):
    if 'o_id' in request.session:

        id = request.session["o_id"]
        sql = 'SELECT * FROM `pg_enquiry` p join pg_details p1 where p.pg_id_id = p1.pg_id and p1.o_id_id = %s;' %id
        obj1 = PG_DETAILS.objects.raw(sql)
        return render(request,"enquiryshow.html",{"data":obj1})
    else:
        return redirect('/owner/error/')



def response(request,id):
    if 'o_id' in request.session:

        obj = ENQUIRY.objects.get(e_id=id)
        return render(request,"response.html",{"data":obj})
    else:
        return redirect('/owner/error/')
def send_res(request,id):
    if 'o_id' in request.session:

        if request.method == "POST":
            #name=request.POST.get("ename")
            #enq=request.POST.get("e_desc")
            #mail=request.POST.get("mail")
            obj=ENQUIRY.objects.get(e_id=id)
            name=obj.e_name
            enq=obj.e_desc
            mail=obj.e_mail
            mess = request.POST.get("res")
            e = mail
            subject = 'Enquiry Status'
            message = f'Dear {name} , Reply for your Enquiry -> {enq} .\n \n \n' \
                       f'RESPONSE : \n'\
                              f'\n \t \t  {mess}'

            email_from = settings.EMAIL_HOST_USER
            recipient_list = [e, ]
            send_mail(subject, message, email_from, recipient_list)
            return redirect("/owner/enqshow/")
    else:
        return redirect(('/owner/error/'))

def add_pgfac(request,id):
    if 'o_id' in request.session:

        pf = PG_FACILITY.objects.filter(pg_id_id=id).values('f_id')
        print("------------------",pf)
        f=[]
        for data in pf:
            f.append(data['f_id'])
        print("---------------------",f)
        obj=FACILITY.objects.all()
        obj1=PG_DETAILS.objects.get(pg_id=id)
        return render(request,"add-pgfac.html",{"fac":obj,"pg":obj1,"pgfac":f})
    else:
        return redirect('/owner/error/')

def ins_pgfac(request,id):
    if 'o_id' in request.session:
        val=request.POST.getlist('fac[]')
        c = len(val)
        print("-----------------FAC ----------",val)
        if c == 0 :
            return redirect("/owner/pg/")
        else:
            print("----------C----------",c)
            for x in val :
                p=PG_FACILITY(f_id_id=x,pg_id_id=id)
                p.save()
        return redirect("/owner/pg/")
    else:
        return redirect('/owner/error/')
