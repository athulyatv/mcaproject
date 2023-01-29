from django.db import models

# Create your models here.
class tbl_stall(models.Model):
    stall_id = models.CharField(max_length=90,primary_key="True")
    stall_number = models.CharField(max_length=30)
    photo = models.CharField(max_length=90)
    descripion = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_stall"

class tbl_customer(models.Model):
    cust_id = models.CharField(max_length=90,primary_key="True")
    cust_name = models.CharField(max_length=30)
    house_name = models.CharField(max_length=90)
    street = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    district= models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    pin_code = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_customer"
        
class tbl_restaurent(models.Model):
    rest_id = models.CharField(max_length=90,primary_key="True")
    rest_name = models.CharField(max_length=30)
    street = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    district= models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    pin_code = models.CharField(max_length=90)
    particulers = models.CharField(max_length=90)
    type = models.CharField(max_length=90)
    rm_name = models.CharField(max_length=90)
    phone = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_restaurent"

class tbl_login(models.Model):
    user_name = models.CharField(max_length=90,primary_key="True")
    cat = models.CharField(max_length=30)
    password = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_login"

class tbl_menu(models.Model):
    menu_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=90)
    description = models.CharField(max_length=90)
    photo = models.CharField(max_length=90)
    unit = models.CharField(max_length=90)
    quantity = models.CharField(max_length=90)
    price = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_menu"

class tbl_table(models.Model):
    table_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    table_no = models.CharField(max_length=90)
    numberof_chair = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    class Meta:
        db_table = "tbl_table"

class tbl_review(models.Model):
    review_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    cust_id = models.ForeignKey(tbl_customer,on_delete=models.CASCADE)
    photo = models.CharField(max_length=90)
    review = models.CharField(max_length=90)
    review_date = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_review"

class tbl_employee(models.Model):
    emp_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    house_name = models.CharField(max_length=90)
    job = models.CharField(max_length=90)
    doj = models.CharField(max_length=90)
    age = models.CharField(max_length=90)
    gender = models.CharField(max_length=90)
    street = models.CharField(max_length=90)
    city = models.CharField(max_length=90)
    district= models.CharField(max_length=90)
    state = models.CharField(max_length=90)
    pin_code = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    status = models.CharField(max_length=90)

    class Meta:
        db_table = "tbl_employee"

class tbl_tablebooking(models.Model):
    tbl_book_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    cust_id = models.ForeignKey(tbl_customer,on_delete=models.CASCADE)
    table_id = models.ForeignKey(tbl_table,on_delete=models.CASCADE)
    date = models.CharField(max_length=90)
    time = models.CharField(max_length=90)
    
  
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_tablebooking"

class tbl_cust_order(models.Model):
    cust_orderid = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    menu_id = models.ForeignKey(tbl_menu,on_delete=models.CASCADE)
    req_quantity = models.CharField(max_length=90)
    amount = models.CharField(max_length=90)
    date = models.CharField(max_length=90)
    
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_cust_order"

class tbl_rest_stall(models.Model):
    r_s_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    stall_id = models.ForeignKey(tbl_stall,on_delete=models.CASCADE)
    
    date = models.CharField(max_length=90)
    
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_rest_stall"

class tbl_leave_application(models.Model):
    appl_id = models.CharField(max_length=90,primary_key="True")
    rest_id = models.ForeignKey(tbl_restaurent,on_delete=models.CASCADE)
    emp_id = models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    leave_appl_date = models.CharField(max_length=90)
    leave_date = models.CharField(max_length=90)
    no_of_days = models.CharField(max_length=90)
    remark = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_leave_application"

class tbl_emp_duty(models.Model):
    emp_duty_id = models.CharField(max_length=90,primary_key="True")
    emp_id = models.ForeignKey(tbl_employee,on_delete=models.CASCADE)
    duty = models.CharField(max_length=90)
    allotment_date = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_emp_duty"

class tbl_payment(models.Model):
    payment_id = models.CharField(max_length=90,primary_key="True")
    cust_orderid = models.ForeignKey(tbl_cust_order,on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=90)
    bank = models.CharField(max_length=90)
    account = models.CharField(max_length=90)
    ifsc = models.CharField(max_length=90)
    amount = models.CharField(max_length=90)
    status = models.CharField(max_length=90)
    
    class Meta:
        db_table = "tbl_payment"

class idgen(models.Model):
    stall_id=models.IntegerField()
    cust_id=models.IntegerField()
    rest_id=models.IntegerField()
    menu_id=models.IntegerField()
    table_id=models.IntegerField()
    review_id=models.IntegerField()
    emp_id=models.IntegerField()
    tbl_book_id=models.IntegerField()
    cust_orderid=models.IntegerField()
    r_s_id=models.IntegerField()
    appl_id=models.IntegerField()
    emp_duty_id=models.IntegerField()
    payment_id=models.IntegerField()
    class Meta:
        db_table = "idgen"
