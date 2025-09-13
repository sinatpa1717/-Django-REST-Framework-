from rest_framework import serializers
from .models import My_model


class Serial(serializers.ModelSerializer):
    class Meta:
        model = My_model
        fields = "__all__"
