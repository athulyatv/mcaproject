# Generated by Django 4.0.4 on 2022-07-06 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_idgen_cust_orderid_tbl_cust_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_cust_order',
            name='menu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tbl_menu'),
        ),
    ]
