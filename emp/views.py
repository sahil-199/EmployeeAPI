from django.shortcuts import render
from .models import Employee
from django.http import JsonResponse,HttpResponse
from .serializer import EmpSerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class EmpList(APIView):

    def get(self,request):
            emp=Employee.objects.all()
            serializer=EmpSerializer(emp,many=True)

            return Response(serializer.data)


class EditEmp(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request,pk):         
            emp=Employee.objects.get(id=pk)
            data=JSONParser().parse(request)
            serializer=EmpSerializer(emp,data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=201)
            return Response(serializer.errors,status=400)





