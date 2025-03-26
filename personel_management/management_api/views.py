from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters import rest_framework as filter
from .serializers import MilitarySerializer, DiplomaSerializer, ChildrenSerializer
from .models import Military, Diploma, Children
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'management_api/register.html', {'form': form})

# Home page 
@login_required
def home(request):
    return render(request, 'management_api/home.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class MilitaryFilter(filter.FilterSet):
    first_name = filter.CharFilter(lookup_expr='icontains')
    rank = filter.CharFilter(lookup_expr='icontains')
    service_number = filter.CharFilter(lookup_expr='icontains')
    

    class Meta:
        model = Military
        fields = ['first_name', 'rank', 'service_number']

class MilitaryViewSet(viewsets.ModelViewSet):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer

    @action(detail=True, methods= ['get'])
    def children(self, request, pk=None):
        military = self.get_object()
        children = military.children.all()
        serializer = ChildrenSerializer(children, many=True)
        return Response(serializer.data)
            
    @action(detail=True, methods=['get'])
    def diplomas(self, request, pk=None):
        military = self.get_object()
        diplomas = military.diplomas.all()
        serializer = DiplomaSerializer(diplomas, many=True)
        return Response(serializer.data)

class ChildrenViewSet(viewsets.ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer

class DiplomaViewSet(viewsets.ModelViewSet):
    queryset = Diploma.objects.all()
    serializer_class = DiplomaSerializer

##################################################################

