from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import MilitarySerializer, DiplomaSerializer, ChildrenSerializer
from .models import Military, Diploma, Children
# Create your views here.

def home(request):
    return render(request, 'management_api/home.html')
  
class MilitaryViewSet(viewsets.ModelViewSet):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [permissions.IsAuthenticated]

class DiplomaViewSet(viewsets.ModelViewSet):
    queryset = Diploma.objects.all()
    serializer_class = DiplomaSerializer
    permission_classes = [permissions.IsAuthenticated]  

class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    permission_classes = [permissions.IsAuthenticated]