# Generated by Django 4.1 on 2023-03-09 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0003_booking_pay_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ENQUIRY',
            fields=[
                ('e_id', models.AutoField(primary_key=True, serialize=False)),
                ('e_desc', models.CharField(max_length=100)),
                ('e_name', models.CharField(max_length=25)),
                ('e_con', models.IntegerField(max_length=13)),
                ('pg_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.pg_details')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pg.user_table')),
            ],
        ),
    ]
