# Generated by Django 4.0.4 on 2022-07-04 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_tbl_employee_house_name_tbl_employee_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='idgen',
            name='tbl_book_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='tbl_tablebooking',
            fields=[
                ('tbl_book_id', models.CharField(max_length=90, primary_key='True', serialize=False)),
                ('date', models.CharField(max_length=90)),
                ('time', models.CharField(max_length=90)),
                ('status', models.CharField(max_length=90)),
                ('cust_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tbl_customer')),
                ('rest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tbl_restaurent')),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tbl_table')),
            ],
            options={
                'db_table': 'tbl_tablebooking',
            },
        ),
    ]