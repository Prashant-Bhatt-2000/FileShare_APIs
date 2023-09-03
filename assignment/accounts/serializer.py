from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from .emailverify import sendemail
from uuid import uuid4



class OpsSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        password = data['password']
        data['password'] = make_password(password)

        email = data.get('email')

        user = User.objects.filter(email=email)

        if user:
            if user.exists():
                raise serializers.ValidationError({'message': 'Email already exists'})
        data['is_ops'] = True

        token = str(uuid4())

        data['verification_token'] = token

        sendemail(email, token)

        return data
    

from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class OpsLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Please enter "email" and "password".')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                
                if user.is_ops and user.is_verified:                
                    refresh = RefreshToken.for_user(user)

                    return {
                            'message': 'Login successful.',
                            'username': user.name,
                            'access': str(refresh.access_token),
                            'refresh': str(refresh),
                            }
                else: 
                    raise serializers.ValidationError('You are not authorise to access this route.')
            else:
                raise serializers.ValidationError('Incorrect email or password.')
        else:
            raise serializers.ValidationError(' Please enter "email" and "password".')



# ==================================================================================================== #


class ClientSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        password = data['password']
        data['password'] = make_password(password)

        email = data.get('email')
        user = User.objects.filter(email=email)
        if user:
            if user.exists():
                raise serializers.ValidationError({'message': 'Email already exists'})
        data['is_client'] = True
        
        token = str(uuid4())

        data['verification_token'] = token

        sendemail(email, token)
        
        return data
    


class ClientLoginSerializer(serializers.Serializer):

    class Meta:
        model = User
        fields = ('email',)
        
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            raise serializers.ValidationError('Please enter "email" and "password".')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                
                if user.is_client and user.is_verified: 
                
                    refresh = RefreshToken.for_user(user)

                    return {
                            'message': 'Login successful.',
                            'username': user.name,
                            'access': str(refresh.access_token),
                            'refresh': str(refresh),
                            }
                else: 
                    raise serializers.ValidationError('You are not authorise to access this route.')

            else:
                raise serializers.ValidationError('Incorrect email or password.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')