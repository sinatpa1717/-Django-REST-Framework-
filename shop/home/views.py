from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import My_model
from rest_framework.response import Response
from .serializers import Serial
from rest_framework import status

# Create your views here.


# home
@api_view(["GET"])
def page_web_api_home(request):
    model = My_model.objects.all()
    serial = Serial(model, many=True)
    return Response(serial.data)


# home-+
@api_view(["GET"])
def page_web_api_up(request):
    model = My_model.objects.all().order_by("data")
    serial = Serial(model, many=True)
    return Response(serial.data)


# home --
@api_view(["GET"])
def page_web_api_down(request):
    model = My_model.objects.all().order_by("-data")
    serial = Serial(model, many=True)
    return Response(serial.data)


# search home
@api_view(["GET"])
def page_web_api_serach(request):
    q = request.GET.get("q")
    if q:
        model = My_model.objects.filter(name__icontains=q)
        serial = Serial(model, many=True)
        return Response(serial.data, status=status.HTTP_200_OK)

    return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)


# tedad
@api_view(["GET"])
def tedad_page(request):
    count = My_model.objects.count()
    return Response({"count": count})
