from django.shortcuts import render, redirect
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, filters
from django_filters import rest_framework as filter
from .serializers import MilitarySerializer, DiplomaSerializer, ChildrenSerializer
from .models import Military, Diploma, Children
from .forms import CustomUserCreationForm
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

class MilitaryFilter(filter.FilterSet):
    title = filter.CharFilter(lookup_expr='icontains')
    author = filter.CharFilter(lookup_expr='icontains')
    registration = filter.NumberFilter(field_name='registration_number', lookup_expr='icontains')
    

    class Meta:
        model = Military
        fields = ['name', 'rank', 'registration_number']

class MilitaryListView(generics.ListAPIView):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filter.DjangoFilterBackend] 
    filterset_class = MilitaryFilter
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'rank', 'registration_number']

class MilitaryDetailView(generics.RetrieveAPIView):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rank', 'name', 'function']

class MilitaryCreateView(generics.CreateAPIView):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [IsAuthenticated]

   
    def perform_create(self, serializer):
        # On peut implementer des modifs sur la vue ici
        serializer.save()

class MilitaryUpdateView(generics.UpdateAPIView):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        # On peut implementer des modifs sur la vue ici
        serializer.save()

class MilitaryDeleteView(generics.DestroyAPIView):
    queryset = Military.objects.all()
    serializer_class = MilitarySerializer
    permission_classes = [IsAuthenticated]