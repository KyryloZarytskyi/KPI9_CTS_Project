from rest_framework import serializers
from .models import Equation
from .models import Message

class EquationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equation
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
