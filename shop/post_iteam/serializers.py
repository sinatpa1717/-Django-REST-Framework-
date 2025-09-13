from .models import post_iteam
from rest_framework import serializers


class Seraill_iteam(serializers.ModelSerializer):
    class Meta :
        model = post_iteam
        fields = "__all__"

