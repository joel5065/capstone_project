from django.urls import path, include
from .views import MilitaryListView, MilitaryCreateView, MilitaryDetailView, MilitaryDeleteView, MilitaryUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
from .views import home, register


urlpatterns = [
    path('register/', register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='management_api/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='management_api/logout.html'), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('home/', home, name='home'), 
    path('military/', MilitaryListView.as_view(), name='military-list'),
    path('military/<int:pk>/', MilitaryDetailView.as_view(), name='military-detail'),
    path('military/create/', MilitaryCreateView.as_view(), name='military-create'),
    path('military/update/<int:pk>', MilitaryUpdateView.as_view(), name='military-update'),
    path('military/delete/<int:pk>', MilitaryDeleteView.as_view(), name='military-delete'),
]