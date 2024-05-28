from django import forms
from pg.models import USER_TABLE, OWNER_TABLE, CATEGORY_TABLE, FEEDBACK_TABLE, PG_DETAILS, BOOKING, PG_FACILITY,\
    FACILITY, AREA

from parsley.decorators import parsleyfy

@parsleyfy
class UserForm(forms.ModelForm):
    class Meta:
        model=USER_TABLE
        fields=["user_id","user_fname","user_lname","user_email","user_pass","user_add","user_con"]


@parsleyfy
class OwnerForm(forms.ModelForm):
    class Meta:
        model=OWNER_TABLE
        fields=["o_id","o_fname","o_lname","o_email","o_pass","o_add","o_con"]

@parsleyfy
class CategoryForm(forms.ModelForm):
    class Meta:
        model=CATEGORY_TABLE
        fields=["c_id","c_name","c_desc"]
@parsleyfy
class PGdetialsForm(forms.ModelForm):
    pg_img=forms.FileField()
    class Meta:
        model=PG_DETAILS
        fields=["pg_id","pg_name","c_id","o_id","pg_email","pg_con","pg_add","pg_img","pg_avail","pg_price","area_id"]

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=FEEDBACK_TABLE
        fields=["f_id","pg_id","user_id","f_desc","f_date"]

class BookingForm(forms.ModelForm):
    class Meta:
        model=BOOKING
        fields=["b_id","pg_id","user_id","b_amt","checkin_date","checkout_date","b_date","b_status","pay_status"]
@parsleyfy
class FacilityForm(forms.ModelForm):
    class Meta:
        model=FACILITY
        fields=["f_id","f_name","f_desc"]
@parsleyfy
class PgFacilityForm(forms.ModelForm):
    class Meta:
        model=PG_FACILITY
        fields=["pgf_id","f_id","pg_id"]
@parsleyfy
class AreaForm(forms.ModelForm):
    class Meta:
        model=AREA
        fields=["area_id","area_name"]

class FacilityForm(forms.ModelForm):
    class Meta:
        model=FACILITY
        fields=["f_id","f_name","f_desc"]

class ImageForm(forms.ModelForm):
    pg_img=forms.FileField()

    class Meta:
        model=PG_DETAILS
        fields=["pg_img"]