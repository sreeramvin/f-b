from django.shortcuts import render
from .models import Todo
from .serializers import Todoserializer
from rest_framework import viewsets,permissions

class Todoclass(viewsets.ModelViewSet):
    queryset=Todo.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class=Todoserializer

def Hi(request):
    return render(request,'todo/hi.html')