from django.db import models


# Create your models here.
class USER_TABLE(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_fname = models.CharField(max_length=15)
    user_lname = models.CharField(max_length=15)
    user_email = models.EmailField(unique=True)
    user_pass = models.CharField(max_length=13)
    user_add = models.CharField(max_length=200)
    user_con = models.CharField(max_length=13)
    is_admin = models.IntegerField(default=0)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField()

    class Meta:
        db_table = "user_table"


class OWNER_TABLE(models.Model):
    o_id = models.AutoField(primary_key=True)
    o_fname = models.CharField(max_length=15)
    o_lname = models.CharField(max_length=15)
    o_email = models.EmailField(unique=True)
    o_pass = models.CharField(max_length=13)
    o_add = models.CharField(max_length=200)
    o_con = models.CharField(max_length=13)
    otp1 = models.CharField(max_length=10, null=True)
    otp_used1 = models.IntegerField()

    class Meta:
        db_table = "owner_table"


class CATEGORY_TABLE(models.Model):
    c_id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=20)
    c_desc = models.CharField(max_length=100)

    class Meta:
        db_table = "cat_table"


class AREA(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=35)

    class Meta:
        db_table = "area"


class PG_DETAILS(models.Model):
    pg_id = models.AutoField(primary_key=True)
    c_id = models.ForeignKey(CATEGORY_TABLE, on_delete=models.CASCADE)
    o_id = models.ForeignKey(OWNER_TABLE, on_delete=models.CASCADE)
    area_id = models.ForeignKey(AREA, on_delete=models.CASCADE)
    pg_email = models.EmailField(unique=True)
    pg_con = models.CharField(max_length=13)
    pg_add = models.CharField(max_length=200)
    pg_img = models.CharField(max_length=100)
    pg_img1 = models.CharField(max_length=100)
    pg_img2 = models.CharField(max_length=100)
    pg_img3 = models.CharField(max_length=100)
    pg_avail = models.IntegerField()
    pg_price = models.IntegerField()
    pg_name = models.CharField(max_length=51)
    pg_desc = models.CharField(max_length=200)
    is_featured = models.IntegerField(default=0)
    reg_date = models.DateField()

    class Meta:
        db_table = "pg_details"


class FEEDBACK_TABLE(models.Model):
    f_id = models.AutoField(primary_key=True)
    pg_id = models.ForeignKey(PG_DETAILS, on_delete=models.CASCADE)
    user_id = models.ForeignKey(USER_TABLE, on_delete=models.CASCADE)
    f_desc = models.CharField(max_length=100)
    f_date = models.DateField()

    class Meta:
        db_table = "feed_table"


class BOOKING(models.Model):
    b_id = models.AutoField(primary_key=True)
    pg_id = models.ForeignKey(PG_DETAILS, on_delete=models.CASCADE)
    user_id = models.ForeignKey(USER_TABLE, on_delete=models.CASCADE)
    b_amt = models.CharField(max_length=6)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    b_date = models.DateField()
    b_status = models.IntegerField(default=0)
    pay_status = models.IntegerField(default=0)
    pay_type=models.IntegerField(default=0)
    class Meta:
        db_table = "book_table"


class FACILITY(models.Model):
    f_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=30)
    f_desc = models.CharField(max_length=100)

    class Meta:
        db_table = "fac_table"


class PG_FACILITY(models.Model):
    pgf_id = models.AutoField(primary_key=True)
    f_id = models.ForeignKey(FACILITY, on_delete=models.CASCADE)
    pg_id = models.ForeignKey(PG_DETAILS, on_delete=models.CASCADE)

    class Meta:
        db_table = "pgfac_table"

class WISHLIST(models.Model):
    w_id=models.AutoField(primary_key=True)
    pg_id=models.ForeignKey(PG_DETAILS,on_delete=models.CASCADE)
    user_id=models.ForeignKey(USER_TABLE,on_delete=models.CASCADE)
    w_date=models.DateField()
    class Meta:
        db_table = "wishlist"

class ENQUIRY(models.Model):
    e_id=models.AutoField(primary_key=True)
    e_mail=models.EmailField(unique=True)
    user_id=models.ForeignKey(USER_TABLE,on_delete=models.CASCADE)
    pg_id=models.ForeignKey(PG_DETAILS,on_delete=models.CASCADE)
    e_desc=models.CharField(max_length=100)
    e_name = models.CharField(max_length=25)
    e_con=models.CharField(max_length=13)