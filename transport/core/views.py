from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Orders, Retail, Driver, Tanker
from .serializers import DriverSerializer, OrderSerializer, TankerSerializer, RetailSerializer



class DriverView(APIView):
    
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Driver.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = DriverSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class TankerView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Tanker.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = TankerSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = TankerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class RetailView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Retail.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = RetailSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class OrderView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Orders.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = OrderSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

