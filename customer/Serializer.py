from rest_framework import serializers
from .models import customer


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = '__all__'

class customercredSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields =('username','password')
