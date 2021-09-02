from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone
from .validators import get_gstin_with_check_digit,datevalid,nonneg,alphanumeric,phoneno,pincode
from django.core.validators import MinLengthValidator

# Create your models here.
class employee(models.Model):
    employee_id = models.AutoField( primary_key=True )
    first_name = models.CharField(max_length=25, default="",validators=[alphanumeric])
    middle_name = models.CharField(max_length=25, default="", blank=True,validators=[alphanumeric])
    last_name = models.CharField(max_length=25, default="",validators=[alphanumeric])
    street = models.CharField(max_length=25, default="")
    phone = models.CharField(max_length=10, default="",validators=[phoneno])
    city = models.CharField(max_length=25, default="")
    pin = models.IntegerField(default=0,validators=[pincode])
    designation = models.CharField(max_length=25, default="")
    
    def __str__(self):
        return str(self.employee_id)


class party(models.Model):
    party_id = models.AutoField( primary_key=True)
    party_name = models.CharField(default="", max_length=35,validators=[alphanumeric])
    gst_number = models.CharField( max_length=15, default="",validators=[get_gstin_with_check_digit])
    employee_id = models.ForeignKey( employee, on_delete=models.CASCADE )

    def __str__(self):
        return str(self.party_id)

class machine(models.Model):
    machine_id = models.AutoField( primary_key=True)
    machine_rpm = models.IntegerField(validators=[nonneg])
    def __str__(self):
        return str(self.machine_id) 
    
class machine_operator(models.Model):
    class Meta:
        unique_together = (('machine_id', 'date'),)
    machine_id= models.ForeignKey(machine, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today,validators=[datevalid])
    employee_id = models.ForeignKey( employee, on_delete=models.CASCADE )
    machine_electricity_consumption = models.FloatField()
    def __str__(self):
        return str(self.machine_id) 

class beam_inward(models.Model):
    class Meta:
        unique_together = (('beam_number','warp_date'),)

    beam_number = models.IntegerField()
    total_meter = models.IntegerField()
    party_id = models.ForeignKey(party, on_delete=models.CASCADE)
    warp_date = models.DateField(auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today,validators=[datevalid])
    def __str__(self):
        return str(self.beam_number)



class yarn(models.Model):
    s_no = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(party, on_delete=models.CASCADE)
    number_of_bags= models.IntegerField(validators=[nonneg])
    gate_pass_number = models.IntegerField(validators=[nonneg])
    weight = models.FloatField()
    def __str__(self):
        return str(self.s_no) 

class wages_report(models.Model):
    employee_id = models.ForeignKey( employee, on_delete=models.CASCADE )
    bill_number = models.AutoField(primary_key=True)
    salary_date = models.DateField( auto_now_add=False, auto_now = False, blank=True, default=datetime.date.today,validators=[datevalid])
    number_of_days = models.IntegerField()
    salary = models.FloatField()
    def __str__(self):
        return str(self.bill_number) 



class bill_details(models.Model):
    class Meta:
        unique_together= (('bill_number', 'item'),)
    bill_number = models.ForeignKey( wages_report, on_delete=models.CASCADE)
    item = models.CharField( max_length = 30, default="")
    def __str__(self):
        return str(self.bill_number)


    
    
class machine_maintenance_report(models.Model):
    store_name = models.CharField(max_length=40, default="")
    total_cost = models.FloatField()
    bill_id = models.AutoField( primary_key=True)
    date = models.DateField( auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today,validators=[datevalid])
    maintenance_date = models.DateField( auto_now_add=False, auto_now=False, blank=True, default=datetime.date.today,validators=[datevalid])
    def __str__(self):
        return str(self.bill_id)



class maintenance_inventory(models.Model):
    class Meta:
        unique_together = (('machine_id', 'part_name', 'bill_id'),)
    bill_id= models.ForeignKey(machine_maintenance_report, on_delete=models.CASCADE)
    machine_id = models.ForeignKey(machine, on_delete=models.CASCADE )
    part_name = models.CharField(max_length =25, default ="" )
    quantity = models.IntegerField()
    def __str__(self):
        return str(self.bill_id)
  
class design(models.Model):
    design_id=models.AutoField( primary_key=True)
    peak =models.CharField(default="", max_length=25)
    cost = models.FloatField()
    colors = models.CharField(default="", max_length=25)

    party_id = models.ForeignKey(party, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.design_id)


class party_bill_delivery(models.Model):
    slip_number = models.AutoField(primary_key=True)
    party_id = models.ForeignKey(party, on_delete=models.CASCADE)
    gst_number = models.CharField(default="", max_length=15,validators=[get_gstin_with_check_digit])
    total_meter_received = models.FloatField()
    total_meter_delivered = models.FloatField()
    peak = models.CharField(default="", max_length=25)
    bill_date = models.DateField( auto_now_add = False, auto_now=False, blank=True, default=datetime.date.today,validators=[datevalid])
    
    def __str__(self):
        return str(self.slip_number) 