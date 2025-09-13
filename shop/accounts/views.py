from django.shortcuts import render
from rest_framework.decorators import APIView
from .serializers import Auth_user
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class MY_ss(APIView):
    def post(self, request):
        user = Auth_user(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data, status=status.HTTP_201_CREATED)
        return Response(user.data, status=status.HTTP_400_BAD_REQUEST)
