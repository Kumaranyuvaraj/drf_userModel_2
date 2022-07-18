from django.shortcuts import render
from .models import User
from .serializers import UserSerializer,UserUpdateSerializer

from django.db.models import Q
from rest_framework.viewsets import ModelViewSet

class UserViewSet(ModelViewSet):
    
    def get_serializer_class(self):
        if self.request.method in ['POST','PUT','PATCH']:
            return UserUpdateSerializer
        return UserSerializer
    
    def get_queryset(self):
        queryset = User.objects.all().order_by('id','email')
        
        if self.request.query_params.get('search',None):
            term = self.request.query_params.get('search')
            first_name_q = Q(first_name__icontains = term)
            last_name_q = Q(last_name__icontains = term)
            queryset = queryset.filter(first_name_q | last_name_q)
            
        return queryset
            
        
            
        
