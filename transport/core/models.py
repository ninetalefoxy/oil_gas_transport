from django.db import models
from django.db.models.deletion import CASCADE


state = (
    ('maharashtra','maharashtra'),
)

fuel = (  ('diesel','diesel'),
    ('gas','gas'),
    ('petrol','petrol')
)

class Retail(models.Model):
    retail_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    state = models.CharField(choices=state, max_length=100)
    district = models.CharField(max_length=100)
    tal = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(models.Model):
    emp_id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    vendor = models.ForeignKey(Retail, on_delete=CASCADE)
    lname = models.CharField(max_length=100)
    license_id = models.CharField(max_length=100)

    def __str__(self):
        return self.fname
    
class Tanker(models.Model):
    truck_id = models.AutoField(primary_key=True)
    veh_type = models.CharField(max_length=100)
    fuel = models.CharField(max_length=100, choices=fuel)
    veh_num = models.CharField(max_length=100)
    maximum_allowed = models.IntegerField()
    estimaion = models.IntegerField()
    current_amount  = models.IntegerField()
    veh_volume = models.IntegerField()
    veh_weight = models.CharField(max_length=100)
    veh_run = models.CharField(max_length=100)

    def __str__(self):
        return str(self.truck_id)
    


status = (
    ('shipping','shipping'),
    ('completed','completed')
)

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    tanker = models.ForeignKey(Tanker, on_delete=CASCADE,related_name='tanker_detail')
    driver = models.ForeignKey(Driver, on_delete=CASCADE,related_name='driver_detail')
    client = models.ForeignKey(Retail,on_delete=CASCADE)
    veh_type = models.CharField(max_length=100,choices=fuel)
    fuel_type = models.CharField(choices=fuel, max_length=100)
    veh_run = models.CharField(max_length=100)
    status = models.CharField(choices=status, max_length=100)
    def __str__(self):
        return str(self.tanker_id)
    


