from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Driver, Orders, Retail, Tanker



class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class RetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = '__all__'

class TankerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanker
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    driver = DriverSerializer(many=False, read_only=True)
    tanker = TankerSerializer(many=False, read_only=True)
    client = RetailSerializer(many=False, read_only=True)
    class Meta:
        model = Orders
        fields = ['order_id','veh_type','fuel_type','veh_run','status','driver','tanker','client']