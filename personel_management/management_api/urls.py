from django.urls import path, include
from .views import MilitaryViewSet, DiplomaViewSet, ChildrenViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import home




router = DefaultRouter()
router.register(r'Military', MilitaryViewSet)
router.register(r'Diploma', DiplomaViewSet)
router.register(r'Children', ChildrenViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('', home, name='home'),
    path('api/', include(router.urls), name="api"),  
]