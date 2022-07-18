from django.urls import path, include
# from rest_framework.authtoken import views as drf_views
from rest_framework.routers import DefaultRouter

from .views import UserViewSet


app_name = 'core'

router = DefaultRouter()
router.register(r'User',UserViewSet,basename='users')

urlpatterns = [
    path('router/', include(router.urls)),

    # path('get-auth-token/', drf_views.obtain_auth_token, name='get_auth_token'),
    
]