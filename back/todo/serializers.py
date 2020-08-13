from .models import Todo
from rest_framework import serializers

class Todoserializer(serializers.ModelSerializer):
    class Meta():
        model=Todo
        fields='__all__'