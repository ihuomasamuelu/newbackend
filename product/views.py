from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.decorators import api_view
from .models import food
from rest_framework import serializers


# Create your views here.

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'


@api_view(['GET'])
def allfood(request):
    allfood = food.objects.all()
    
    serializer = FoodSerializer(allfood, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def createfood(request):
    return Response(request.data)