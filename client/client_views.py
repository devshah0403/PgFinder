import sys
from datetime import date, datetime

from django.contrib import messages
from django.shortcuts import render, redirect

from pg.forms import UserForm, FeedbackForm , OwnerForm
from pg.models import *
from pgfinder import settings


def main(request):
    obj=PG_DETAILS.objects.all()
    obj1=AREA.objects.all()

    # sql = "SELECT pg_id_id FROM wishlist where user_id_id=uid;"
    #obj2 = WISHLIST.objects.raw(sql)
    #for data in obj1:
    #   obj2=PG_DETAILS.objects.filter(area_id=data).count()

    sql = "SELECT 1 as pg_id, a.area_name , a.area_id , count(*) as total  FROM pg_details p join area a where p.area_id_id = a.area_id GROUP by area_id_id;"
    obj1 = AREA.objects.raw(sql);
    p = PG_DETAILS.objects.all()
    likes = []

    if 'u_id' in request.session:

        uid = request.session['u_id']
        for data in p:
            c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
            if c > 0:
                likes.append(data.pg_id)
                c = 0
        print("========", likes)

        return render(request, "home.html",{"form":obj,"data":obj1,"likes":likes})
    else:
        likes=[]
        return render(request, "home.html", {"form": obj, "data": obj1, "likes": likes})

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = USER_TABLE.objects.filter(user_email=email, user_pass=password).count()
        if val == 1:
            return redirect("/client/shop/")
        else:
            messages.error(request, "Invalid Username and Password")
            return redirect("/client/userlogin/")

    else:
        return render(request, "userlogin.html")


#################################################################################################################
def UserLogin(request):

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = USER_TABLE.objects.filter(user_email=email, user_pass=password).count()
        if val == 1:
            data = USER_TABLE.objects.filter(user_email=email, user_pass=password)
            for i in data:
                request.session['u_id'] = i.user_id
                request.session['u_fname'] = i.user_fname
                request.session['u_lname'] = i.user_lname
                request.session['u_email'] = i.user_email
            if request.POST.get("rem"):
                response = redirect("/client/main/")
                response.set_cookie('c_uemail', request.POST["email"], 3600 * 24 * 365 * 2)
                response.set_cookie('c_upass', request.POST["password"], 3600 * 24 * 365 * 2)
                return response
            return redirect("/client/main/")
        else:
            messages.error(request, "Invalid Username and Password")
            return redirect("/client/userlogin/")

    else:
        if request.COOKIES.get('c_uemail'):
            return render(request, "userlogin.html",
                          {'u_email_cookie': request.COOKIES['c_uemail'], 'u_pass_cookie': request.COOKIES['c_upass']})
        else:
            return render(request, "userlogin.html")

    return redirect("/login")


def UserLogout(request):
    try:
        del request.session['u_id']
        del request.session['u_fname']
        del request.session['u_lname']
        del request.session['u_email']
        del request.session['area_id']
        del request.session['fac1']
    except:
        pass
    return redirect('/client/userlogin/')


def UserForgot(request):
    return render(request, "forgot_c.html")


from django.core.mail import send_mail
import random


def UserSendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e

    obj = USER_TABLE.objects.filter(user_email=e).count()

    if obj == 1:
        val = USER_TABLE.objects.filter(user_email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification for PG-Finder'
        message = 'One-Time Password for PG-Finder :' + str(otp1) + " \n \n  Don't share it with anyone."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'password_c.html')
    else:
        messages.error(request,"Invalid Email.")
        return render(request,"forgot_c.html")

def UserPassword(request):
    if request.method == "POST":

        C_otp = request.POST['otp']
        C_pass = request.POST['pass']
        C_cpass = request.POST['cpass']

        if C_pass == C_cpass:

            e = request.session['temail']
            val = USER_TABLE.objects.filter(user_email=e, otp=C_otp, otp_used=0).count()

            if val == 1:
                USER_TABLE.objects.filter(user_email=e).update(otp_used=1, user_pass=C_pass)
                return redirect("/client/userlogin")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "forgot_c.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "password_c.html")

    else:
        return redirect("/client/userforgot")


def UserRegister(request):
    return render(request, "register.html")


def insertUser(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        print("-------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/userlogin/")
            except:
                print("----------", sys.exc_info())
    else:
        form = UserForm()
    return render(request, "register.html", {"form": form})
def main(request):
    obj=PG_DETAILS.objects.all()
    obj1=AREA.objects.all()

    # sql = "SELECT pg_id_id FROM wishlist where user_id_id=uid;"
    #obj2 = WISHLIST.objects.raw(sql)
    #for data in obj1:
    #   obj2=PG_DETAILS.objects.filter(area_id=data).count()

    sql = "SELECT 1 as pg_id, a.area_name , a.area_id , count(*) as total  FROM pg_details p join area a where p.area_id_id = a.area_id GROUP by area_id_id;"
    obj1 = AREA.objects.raw(sql);
    p = PG_DETAILS.objects.all()
    likes = []

    if 'uid' in request.session:

        uid = request.session['u_id']
        for data in p:
            c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
            if c > 0:
                likes.append(data.pg_id)
                c = 0
        print("========", likes)

        return render(request, "home.html",{"form":obj,"data":obj1,"likes":likes})
    else:
        likes=[]
        return render(request, "home.html", {"form": obj, "data": obj1, "likes": likes})


def shop(request):

    f = FACILITY.objects.all()
    p = PG_DETAILS.objects.all()
    likes=[]

    if 'u_id' in request.session:

        uid = request.session['u_id']
        for data in p:
            c = WISHLIST.objects.filter(user_id_id = uid,pg_id_id=data.pg_id).count()
            if c > 0:
                likes.append(data.pg_id)
                c=0
        print("========",likes)

        if 'area_id' in request.session:
            del request.session['area_id']
        if "fac1" in request.session:
            del request.session['fac1']

        return render(request, "shop.html", {'pg_details': p,"fac":f,"likes":likes})
    else:
        if 'area_id' in request.session:
            del request.session['area_id']
        if "fac1" in request.session:
            del request.session['fac1']

        likes=[]
        return render(request, "shop.html", {'pg_details': p, "fac": f, "likes": likes})


def product_details(request, id):
    obj = PG_DETAILS.objects.filter(pg_id=id).first()
    obj1 = FEEDBACK_TABLE.objects.filter(pg_id_id=id)
    obj2=FEEDBACK_TABLE.objects.filter(pg_id_id=id).count()
    obj3=PG_FACILITY.objects.filter(pg_id_id=id)

    return render(request, "product-details.html", {"pg_details": obj, "feed_table": obj1,"form":obj2,"data":obj3})


def InsFeedback(request):
    if 'u_id' in request.session:
        try:
            d = date.today()
            p_id = request.POST["pg_id"]
            print("===========", p_id)
            des = request.POST["desc"]
            uid = request.session['u_id']
            f = FEEDBACK_TABLE(f_date=d, f_desc=des, pg_id_id=p_id, user_id_id=uid)
            f.save()
            return redirect("/client/product-details/%s" % p_id)

        except:
            print("-------------------", sys.exc_info())

        return render(request, "product-details.html")
    else:
        return redirect("/client/userlogin/")

def listing(request):
    return render(request, "add-listing.html")


def contact(request):
    obj = PG_DETAILS.objects.all()
    if "u_id" in request.session:
        id=request.session["u_id"]
        obj1=USER_TABLE.objects.filter(user_id=id)
        return render(request, "contact.html", {'form': obj,"data":obj1})
    else:
        return render(request,"contact.html",{'form':obj})




def ins_enquiry(request):
    if request.method == "POST":
        if "u_id" in request.session:
            id=request.session["u_id"]
            name=request.POST["uname"]
            email=request.POST["uemail"]
            pg=request.POST["pg_list"]
            con=request.POST["ucon"]
            enq=request.POST["desc"]
            e=ENQUIRY(user_id_id=id,pg_id_id=pg,e_desc=enq,e_name=name,e_con=con,e_mail=email)
            e.save()
            return redirect('/client/contact/')
        else:
            name = request.POST["uname"]
            email = request.POST["uemail"]
            pg = request.POST["pg_list"]
            con = request.POST["ucon"]
            enq = request.POST["desc"]
            e = ENQUIRY(pg_id_id=pg, e_desc=enq, e_name=name, e_con=con,e_mail=email)
            e.save()
            return redirect('/client/contact/')

def account(request):
    if 'u_id' in request.session:

        uid = request.session['u_id']
        obj = USER_TABLE.objects.filter(user_id=uid).first()
        return render(request, 'myaccount.html', {"user_table": obj})
    else:
        return redirect('/client/userlogin/')




def updateProfile(request):
    if request.method == "POST":
        uid=request.session['u_id']
        fname=request.POST['user_fname']
        lname = request.POST['user_lname']
        con = request.POST['user_con']
        email = request.POST['user_email']
        add = request.POST['user_add']
        USER_TABLE.objects.filter(user_id=uid).update(user_fname=fname,user_lname=lname,user_con=con,user_email=email,user_add=add)
        return redirect("/client/myaccount/")
    else:
        return redirect("/client/myaccount/")

def open_date(request,id):
    obj=PG_DETAILS.objects.filter(pg_id=id).first
    d=date.today()
    today_date=d.strftime('%Y-%m-%d')

    return render(request,'booking.html',{"pg_details":obj,"today_date":today_date})


def booking(request, id):
    obj = PG_DETAILS.objects.get(pg_id=id)
    obj1 = PG_DETAILS.objects.filter(pg_id=id).first()

    try:
        p_id = id
        uid = request.session['u_id']
        d = date.today()
        cin = request.POST["checkin_date"]
        cout = request.POST["checkout_date"]
        print("***********", cout, "************", cin)
        ci = str(cin)
        co = str(cout)
        r = days_between(ci, co)
        print("-----------------------",r)
        pay=request.POST.get('cash')
        amt = obj.pg_price
        print("===========", p_id)
        if r < 0:
            messages.error(request, "Please Select Valid check out date")
            print("[[[[[[[[[[[[[[]]]]]]]]]]]]]]]]]]")
            return render(request,"booking.html")
        else:
            b = BOOKING(pg_id_id=p_id, user_id_id=uid, b_date=d, checkin_date=cin, checkout_date=cout, b_amt=amt,pay_type=pay)
            b.save()
            return redirect('/client/cart/')

        #o=WISHLIST.objects.filter(pg_id_id=p_id).delete()
    except:
        print("-------------------", sys.exc_info())

    # return redirect("/client/cart/")


def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return ((d2 - d1).days)





def changePassword(request):
    if request.method == "POST":
        uid = request.session['u_id']
        old = request.POST['old']
        new = request.POST['pass']
        con = request.POST['cpass']
        obj = USER_TABLE.objects.get(user_id=uid)
        text = obj.user_pass
        if (old == text):
            if (new == con):
                USER_TABLE.objects.filter(user_id=uid).update(user_pass=new)
                return redirect("/client/myaccount/")
            else:
                messages.error(request, "New Password And Confirm Password Didn't Match")
                return render(request, "myaccount.html")
        else:
            messages.error(request, "Please Enter A Valid Password")
            return render(request, "myaccount.html")

    else:
        return redirect("/client/myaccount/")

def cart(request):

    if request.method == "POST":
        id=request.POST.get('bid')
        val = BOOKING.objects.filter(b_id=id).update(pay_status=1)
    uid = request.session['u_id']
    obj = BOOKING.objects.filter(user_id=uid).all()
    obj1 = BOOKING.objects.filter(user_id=uid).all().count()
    return render(request,"cart.html",{'form':obj,"count":obj1})

def OwnerLogin(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = OWNER_TABLE.objects.filter(o_email=email, o_pass=password).count()
        if val == 1:
            data = OWNER_TABLE.objects.filter(o_email=email, o_pass=password)
            for i in data:
                request.session['o_id'] = i.o_id
                request.session['o_fname'] = i.o_fname
                request.session['o_lname'] = i.o_lname
                request.session['o_email'] = i.o_email
            if request.POST.get("rem"):
                response = redirect("/owner/show/")
                response.set_cookie('o_uemail', request.POST["email"], 3600 * 24 * 365 * 2)
                response.set_cookie('o_upass', request.POST["password"], 3600 * 24 * 365 * 2)
                return response
            return redirect("/owner/o_dashboard/")
        else:
            messages.error(request, "Invalid Username and Password")
            return redirect("/client/ownerlogin/")

    else:
        if request.COOKIES.get('o_uemail'):
            return render(request, "ownerlogin.html",
                          {'o_email_cookie': request.COOKIES['o_uemail'], 'o_pass_cookie': request.COOKIES['o_upass']})
        else:
            return render(request, "ownerlogin.html")

    return redirect("/client/ownerlogin/")


from django.http import JsonResponse


def autosuggest(request):
    print("-------- Auto Suggest Call -------")
    if 'term' in request.GET:
        qs = AREA.objects.filter(area_name__istartswith=request.GET.get('term'))

        names = list()

        for x in qs:
            names.append(x.area_name)
        return JsonResponse(names, safe=False)
    return render(request, "shop.html")


def search(request):
    if request.method == "POST":
        name = request.POST["area_name"]
        f=FACILITY.objects.all()
        if name != '':

            obj1 = AREA.objects.filter(area_name=name).count()
            print("2222222222222222222222222222",obj1)
            if obj1 == 0:
                return redirect('/client/c_404/')
            else:
                obj = AREA.objects.get(area_name=name)
            aid = obj.area_id
            request.session['area_id'] = aid
            prod = PG_DETAILS.objects.filter(area_id_id=aid).all()
            pro = PG_DETAILS.objects.filter(area_id_id=aid).count()
            p = PG_DETAILS.objects.all()
            likes = []

            if 'u_id' in request.session:

                uid = request.session['u_id']
                for data in p:
                    c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
                    if c > 0:
                        likes.append(data.pg_id)
                        c = 0
                print("========", likes)

                if pro == 0:
                    return redirect('/client/c_404/')
                else:
                    prod = PG_DETAILS.objects.filter(area_id_id=aid)
                    p = PG_DETAILS.objects.all()
                    likes = []
                    uid = request.session['u_id']
                    for data in p:
                        c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
                        if c > 0:
                            likes.append(data.pg_id)
                            c = 0
                    print("========", likes)
                return render(request, 'shop.html', {'pg_details': prod, "likes": likes,"fac":f})
            else:
                return render(request, 'shop.html', {'pg_details': prod, "likes": likes,"fac":f})
        else:
            obj=PG_DETAILS.objects.all()
            return render(request,'shop.html',{"pg_details":obj,"fac":f})


    else:
        prod = PG_DETAILS.objects.all()
    return render(request, 'shop.html', {'pg_details': prod})

def location(request,id):
    obj=PG_DETAILS.objects.filter(area_id_id=id)
    request.session['area_id'] = id
    p = PG_DETAILS.objects.all()
    likes = []
    if 'u_id' in request.session:
        uid = request.session['u_id']
        for data in p:
            c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
            if c > 0:
                likes.append(data.pg_id)
                c = 0
        print("========", likes)
        f = FACILITY.objects.all()
        return render(request,'shop.html',{'pg_details':obj,"likes":likes,"fac":f})
    else:
        f = FACILITY.objects.all()
        return render(request, 'shop.html', {'pg_details': obj, "likes": likes,"fac":f})
def insert_wishlist(request,id):
    if 'u_id' in request.session :
        try:
            uid=request.session['u_id']
            wd=date.today()
            w=WISHLIST(w_date=wd,user_id_id=uid,pg_id_id=id)
            w.save()
            return redirect('/client/showwish/')
        except:
            print("-------------------", sys.exc_info())
        return redirect('/client/showwish/')
    else:
        return redirect('/client/userlogin/')
def show_wishlist(request):
    uid = request.session['u_id']
    obj=WISHLIST.objects.filter(user_id=uid)
    obj1=WISHLIST.objects.filter(user_id=uid).count()
    print("---------------",obj)
    return render(request,'wishlist.html',{'form':obj,"count":obj1})
def delete_wishlist(request,id):
    uid = request.session['u_id']
    obj=WISHLIST.objects.filter(w_id=id).delete()
    return redirect('/client/showwish/')

def del_pg_wish(request,id):
    uid=request.session['u_id']
    obj = WISHLIST.objects.filter(pg_id_id=id).delete()
    return redirect('/client/shop/')


def error(request):
    return render(request,'c_404.html')

def sort_product(request):
    sid = request.GET.get('sort')
    print("Ajx value -----" +sid)
    #subcat_id = request.session['s_id']
    #print("-----------session ---",request.session['s_id'])
    if sid == '1':
        print("----------- SORT PRODUCTS------" +sid)

        if 'area_id' in request.session :
            aid =request.session['area_id']
            results = PG_DETAILS.objects.filter(area_id_id = aid).order_by("pg_price")
        else:
            results=PG_DETAILS.objects.all().order_by("pg_price")
    else:
        print("----------- SORT PRODUCTS------" +sid)
        if 'area_id' in request.session:
            aid = request.session['area_id']
            results = PG_DETAILS.objects.filter(area_id_id=aid).order_by("-pg_price")
        else:
            results = PG_DETAILS.objects.all().order_by("-pg_price")
    return render(request,'sort.html',{'p':results})


def OwnerForgot(request):
    return render(request,"ownerforgot.html")

def OwnerSendotp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e

    obj = OWNER_TABLE.objects.filter(o_email=e).count()

    if obj == 1:
        val = OWNER_TABLE.objects.filter(o_email=e).update(otp1=otp1, otp_used1=0)

        subject = 'OTP Verification for PG-Finder'
        message = 'One-Time Password for PG-Finder(Owner) :' + str(otp1) + " \n \n Don't share it with anyone."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'password_o.html')
    else:
        messages.error(request,"Invalid Email")
        return redirect('/client/ownerforgot/')

def OwnerPassword(request):
    if request.method == "POST":

        O_otp = request.POST['otp']
        O_pass = request.POST['pass']
        O_cpass = request.POST['cpass']

        if O_pass == O_cpass:

            e = request.session['temail']
            val = OWNER_TABLE.objects.filter(o_email=e, otp1=O_otp, otp_used1=0).count()

            if val == 1:
                OWNER_TABLE.objects.filter(o_email=e).update(otp_used1=1, o_pass=O_pass)
                return redirect("/client/ownerlogin")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "ownerforgot.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "password_o.html")

    else:
        return redirect("/client/ownerforgot")

def OwnerRegister(request):
    return render(request, "ownerregister.html")


def insertOwner(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        print("-------------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect("/client/ownerlogin/")
            except:
                print("----------", sys.exc_info())
    else:
        form = OwnerForm()
    return render(request, "ownerregister.html", {"form": form})

def load_menu(request):
    c = AREA.objects.all()
    return render(request,"test.html",{"cat":c})

def filter(request):
    print("---------- POST ----------")
    if request.method=="POST":
        c=request.POST.getlist("check[]")
        print("----------------",c)
        obj = PG_DETAILS.objects.all().values('pg_id')
        request.session["fac1"]=1;

        if 'area_id' in request.session:
            print("-----------AREA--------------")
            aid=request.session['area_id']
            obj = PG_DETAILS.objects.filter(area_id=aid).values('pg_id')
            for x in c:
                obj=PG_FACILITY.objects.filter(f_id_id=x,pg_id_id__in=obj).values('pg_id')
                print("-----------",obj)

            obj1 = PG_DETAILS.objects.filter(pg_id__in=obj)
            obj2=FACILITY.objects.all()
            print("--------------",obj1)
        else:
            for x in c:
                obj=PG_FACILITY.objects.filter(f_id_id=x,pg_id_id__in=obj).values('pg_id')
                print("-----------",obj)

            obj1 = PG_DETAILS.objects.filter(pg_id__in=obj)
            obj2=FACILITY.objects.all()
            print("--------------",obj1)
        request.session['fac'] = c
        p = PG_DETAILS.objects.all()
        likes = []
        if 'uid' in request.session:

            uid = request.session['u_id']
            for data in p:
                c = WISHLIST.objects.filter(user_id_id=uid, pg_id_id=data.pg_id).count()
                if c > 0:
                    likes.append(data.pg_id)
                    c = 0
            print("========", likes)

            return render(request,"shop.html",{"pg_details":obj1,"fac":obj2,"likes":likes})
        else:
            likes = []
            return render(request, "shop.html", {"pg_details": obj1, "fac": obj2, "likes": likes})

def filter_product(request):
    s = request.GET.get('start')
    e = request.GET.get('end')

    print("Ajx filter value -----", s, "---", e)

    if 'area_id' in request.session:
        aid = request.session['area_id']
        results = PG_DETAILS.objects.filter(area_id_id = aid, pg_price__range=[s, e])
    else:
        results = PG_DETAILS.objects.filter(pg_price__range=[s, e])
        print("----------------",results)

    return render(request, 'sort.html', {'p': results})

def short_category(request):
    if request.method == "POST":
        n = request.POST.get("id")
        print("000000000000000000000000000", n)
        if 'area_id' in request.session:
            aid=request.session['area_id']
            p = PG_DETAILS.objects.filter(c_id_id=n,area_id_id=aid)
            for data in p:
                print("000000000000000000000000000",data)
            f=FACILITY.objects.all()
        else:
            p = PG_DETAILS.objects.filter(c_id_id=n)
            for data in p:
                print("000000000000000000000000000", data)
            f = FACILITY.objects.all()
        return render(request,"shop.html",{"pg_details":p,"fac":f})
    else:
        p = PG_DETAILS.objects.all()
        f = FACILITY.objects.all()
    return render(request, "shop.html", {"pg_details":p,"fac":f})



