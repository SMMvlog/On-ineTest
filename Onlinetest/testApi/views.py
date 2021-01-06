from rest_framework import viewsets
from .models import CreateTest,StudentModel
from .serializers import CreateTestSerializer,StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser
# Create your views here.

class CreateView(viewsets.ModelViewSet):
    queryset = CreateTest.objects.all()
    serializer_class = CreateTestSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAdminUser]

class StudentAns(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

