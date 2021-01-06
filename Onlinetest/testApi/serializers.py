from .models import CreateTest,StudentModel
from rest_framework import serializers

class CreateTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateTest
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = "__all__"