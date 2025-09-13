from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import post_iteam
from .serializers import Seraill_iteam
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def post_page_web_iteam(request):
    model = post_iteam.objects.create()
    if model:
        serial = Seraill_iteam(data=request.data)
        return Response (serial.data, status=status.HTTP_201_CREATED)
    return Response (serial.data, status=status.HTTP_400_BAD_REQUEST)

