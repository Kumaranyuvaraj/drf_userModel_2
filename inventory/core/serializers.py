from rest_framework import serializers
from .models import User

class UserUpdateSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length=16,min_length = 6,write_only=True,required=True)
    
    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name','mobile','address','password','is_active','is_staff','is_superuser')
        
    def create(self,validated_data):
        user = User.objects.create_user (
            email = validated_data.get('email'),
            first_name = validated_data.get('first_name'),
            last_name = validated_data.get('last_name'),
            mobile = validated_data.get('mobile'),
            address = validated_data.get('address'),
            password = validated_data.get('password'),
            is_active = validated_data.get('is_active'),
            is_staff = validated_data.get('is_staff'),
            is_superuser = validated_data.get('is_superuser')
        )
        
        return user
    
    def update(self, instance, validated_data):
        
        password = validated_data.get('password',None)
        
        if 'password' in validated_data:
            del validated_data['password']
            
        user = super().update(instance, validated_data)
        
        if password:
            user.set_password(password)
            user.save()
            
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name','mobile','address','is_active','is_staff','is_superuser')
            
            
            
        
        
        
        
        
 