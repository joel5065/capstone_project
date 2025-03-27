from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import viewsets
from django_filters import rest_framework as filters
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
###############################################################################
class MilitaryFilter(filters.FilterSet):
    rank = filters.ChoiceFilter(choices=Military.RANK_CHOICES)
    date_of_birth = filters.DateFilter(field_name='date_of_birth', lookup_expr='gte')
    current_unit = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')
    service_number = filters.CharFilter(lookup_expr='icontains')
    graduation_school = filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Military
        fields = ['rank', 'current_unit', 'first_name', 'last_name', 'service_number']

class ChildrenFilter(filters.FilterSet):
    date_of_birth = filters.DateFilter(field_name='date_of_birth', lookup_expr='gte')
    gender = filters.ChoiceFilter(choices=[('M', 'Male'), ('F', 'Female')])
    grade = filters.CharFilter(lookup_expr='icontains')
    first_name = filters.CharFilter(lookup_expr='icontains')
    last_name = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Children
        fields = ['first_name','gender', 'grade', 'military']

class DiplomaFilter(filters.FilterSet):
    institution = filters.CharFilter(lookup_expr='icontains')
    degree = filters.CharFilter(lookup_expr='icontains')
    field_of_study = filters.CharFilter(lookup_expr='icontains')
    graduation_date = filters.DateFilter(field_name='graduation_date', lookup_expr='gte')
    diploma_number = filters.CharFilter(lookup_expr='icontains')
    type_of_diploma = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Diploma
        fields = ['institution', 'degree', 'field_of_study','diploma_number', 'type_of_diploma', 'military'] 
##################################################################################################

class MilitaryViewSet(viewsets.ModelViewSet):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    filter_class = MilitaryFilter
    search_fields = ['rank', 'current_unit', 'first_name', 'last_name', 'service_number']
    ordering_fields = ['rank', 'first_name', 'last_name', 'service_number','current_unit']
    ordering = ['last_name']

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
    filter_class = ChildrenFilter
    search_fields = ['first_name','gender', 'grade', 'military']
    ordering_fields = ['first_name','last_name','gender', 'date_of_birth', 'gender', 'military']
    ordering = ['last_name']

class DiplomaViewSet(viewsets.ModelViewSet):
    queryset = Diploma.objects.all()
    serializer_class = DiplomaSerializer
    filter_class = DiplomaFilter
    search_fields = ['institution', 'degree', 'field_of_study','diploma_number', 'type_of_diploma', 'military']
    ordering_fields = ['degree', 'field_of_study','diploma_number', 'type_of_diploma','institution']
    ordering = ['last_name']

##################################################################

