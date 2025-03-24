from django.urls import path, include
from .views import MilitaryListView, MilitaryCreateView, MilitaryDetailView, MilitaryDeleteView, MilitaryUpdateView
from rest_framework.authtoken.views import obtain_auth_token
from .views import home


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', home, name='home'),
    #path('api/', include(router.urls), name="api"),  
    path('military/', MilitaryListView.as_view(), name='military-list'),
    path('military/<int:pk>/', MilitaryDetailView.as_view(), name='military-detail'),
    path('military/create/', MilitaryCreateView.as_view(), name='military-create'),
    path('military/update/<int:pk>', MilitaryUpdateView.as_view(), name='military-update'),
    path('military/delete/<int:pk>', MilitaryDeleteView.as_view(), name='military-delete'),
]