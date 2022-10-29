from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import ToDoList

# Create your views here.

class MainView(APIView):
    def get(self, request):
        return Response({'ок?':'ок'})

class ToDoListView(APIView):
    def get(self, request):
        ToDoList_obj = ToDoList.objects.get(id=1)
        return Response(model_to_dict(ToDoList_obj))

    def get(self, request, time=None):
        ToDoList_obj = ToDoList.objects.get(id=1)
        if until_data <= time:
            return True

        ToDoList_obj.save()

        return Response(model_to_dict(ToDoList_obj))



