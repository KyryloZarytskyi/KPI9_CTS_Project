from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Equation
from .models import Message
from .serializers import EquationSerializer 

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.db import transaction

# Create your views here.

class EquationView(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description="Equation ID")
        ],
        responses={
            200: openapi.Response('Equation found', EquationSerializer),
            404: openapi.Response('Equation not found')
        },
    )
    def get(self, request, id):
        try:
            equation = Equation.objects.get(pk=id)
        except Equation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = EquationSerializer(equation)
        return Response(serializer.data)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description="Equation ID")
        ],
        request_body=EquationSerializer,
        responses={
            200: openapi.Response('Equation created', EquationSerializer),
            400: openapi.Response('Invalid data')
        },
    )
    @transaction.atomic
    def post(self, request, id):
        #check if exists
        if(Equation.objects.filter(pk=id).exists()):
            return Response(status=status.HTTP_409_CONFLICT)
        equation = Equation(pk=id)
        data_copy = request.data.copy()
        data_copy['id'] = id
        eq_serializer = EquationSerializer(equation, data=data_copy)
        if eq_serializer.is_valid():
            eq_serializer.save()
            message = Message(message="Equation created")
            message.save()
            return Response(eq_serializer.data)
        return Response(eq_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('id', openapi.IN_PATH, type=openapi.TYPE_INTEGER, description="Equation ID")
        ],
        request_body=EquationSerializer,
        responses={
            200: openapi.Response('Equation updated', EquationSerializer),
            400: openapi.Response('Invalid data')
        },
    )
    def put(self, request, id):
        try:
            equation = Equation.objects.get(pk=id)
        except Equation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        data_copy = request.data.copy()
        data_copy['id'] = id
        serializer = EquationSerializer(equation, data=data_copy)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
