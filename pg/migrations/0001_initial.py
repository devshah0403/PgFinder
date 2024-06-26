# Generated by Django 4.1 on 2023-02-25 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AREA',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=35)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='CATEGORY_TABLE',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=20)),
                ('c_desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cat_table',
            },
        ),
        migrations.CreateModel(
            name='FACILITY',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_name', models.CharField(max_length=30)),
                ('f_desc', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'fac_table',
            },
        ),
        migrations.CreateModel(
            name='OWNER_TABLE',
            fields=[
                ('o_id', models.AutoField(primary_key=True, serialize=False)),
                ('o_fname', models.CharField(max_length=15)),
                ('o_lname', models.CharField(max_length=15)),
                ('o_email', models.EmailField(max_length=254, unique=True)),
                ('o_pass', models.CharField(max_length=13)),
                ('o_add', models.CharField(max_length=200)),
                ('o_con', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'owner_table',
            },
        ),
        migrations.CreateModel(
            name='PG_DETAILS',
            fields=[
                ('pg_id', models.AutoField(primary_key=True, serialize=False)),
                ('pg_email', models.EmailField(max_length=254, unique=True)),
                ('pg_con', models.CharField(max_length=13)),
                ('pg_add', models.CharField(max_length=200)),
                ('pg_img', models.CharField(max_length=100)),
                ('pg_img1', models.CharField(max_length=100)),
                ('pg_img2', models.CharField(max_length=100)),
                ('pg_img3', models.CharField(max_length=100)),
                ('pg_avail', models.IntegerField()),
                ('pg_price', models.CharField(max_length=7)),
                ('pg_name', models.CharField(max_length=51)),
                ('pg_desc', models.CharField(max_length=200)),
                ('is_featured', models.IntegerField(default=0)),
                ('reg_date', models.DateField()),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.area')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.category_table')),
                ('o_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.owner_table')),
            ],
            options={
                'db_table': 'pg_details',
            },
        ),
        migrations.CreateModel(
            name='USER_TABLE',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_fname', models.CharField(max_length=15)),
                ('user_lname', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('user_pass', models.CharField(max_length=13)),
                ('user_add', models.CharField(max_length=200)),
                ('user_con', models.CharField(max_length=13)),
                ('is_admin', models.IntegerField(default=0)),
                ('otp', models.CharField(max_length=10, null=True)),
                ('otp_used', models.IntegerField()),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
        migrations.CreateModel(
            name='WISHLIST',
            fields=[
                ('w_id', models.AutoField(primary_key=True, serialize=False)),
                ('w_date', models.DateField()),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.pg_details')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.user_table')),
            ],
            options={
                'db_table': 'wishlist',
            },
        ),
        migrations.CreateModel(
            name='PG_FACILITY',
            fields=[
                ('pgf_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.facility')),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.pg_details')),
            ],
            options={
                'db_table': 'pgfac_table',
            },
        ),
        migrations.CreateModel(
            name='FEEDBACK_TABLE',
            fields=[
                ('f_id', models.AutoField(primary_key=True, serialize=False)),
                ('f_desc', models.CharField(max_length=100)),
                ('f_date', models.DateField()),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.pg_details')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.user_table')),
            ],
            options={
                'db_table': 'feed_table',
            },
        ),
        migrations.CreateModel(
            name='BOOKING',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_amt', models.CharField(max_length=6)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('b_date', models.DateField()),
                ('b_status', models.IntegerField(default=0)),
                ('pay_status', models.IntegerField(default=0)),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.pg_details')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.user_table')),
            ],
            options={
                'db_table': 'book_table',
            },
        ),
    ]
