from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from django.contrib.auth import views as auth_views
from .views import home, register, logout_view, MilitaryViewSet, DiplomaViewSet, ChildrenViewSet

router = DefaultRouter()
router.register(r'military', MilitaryViewSet)
router.register(r'children', ChildrenViewSet)
router.register(r'diplomas', DiplomaViewSet)

urlpatterns = [
    path('register/', register, name='register'),
    path('', auth_views.LoginView.as_view(template_name='management_api/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/', include(router.urls)),
    path('home/', home, name='home'), 

]