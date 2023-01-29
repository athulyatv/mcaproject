# Generated by Django 4.0.4 on 2022-07-01 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_tbl_review_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='idgen',
            name='emp_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='tbl_employee',
            fields=[
                ('emp_id', models.CharField(max_length=90, primary_key='True', serialize=False)),
                ('job', models.CharField(max_length=90)),
                ('doj', models.CharField(max_length=90)),
                ('age', models.CharField(max_length=90)),
                ('gender', models.CharField(max_length=90)),
                ('street', models.CharField(max_length=90)),
                ('city', models.CharField(max_length=90)),
                ('district', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('pin_code', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=90)),
                ('status', models.CharField(max_length=90)),
                ('rest_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tbl_restaurent')),
            ],
            options={
                'db_table': 'tbl_employee',
            },
        ),
    ]
