from rest_framework import serializers
from WebApp.models import Employee 

class WebAppSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee 
    fields = '__all__'