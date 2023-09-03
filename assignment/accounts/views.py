from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import OpsSerializer, OpsLoginSerializer, ClientSerializer, ClientLoginSerializer
from .models import User

# Create your views here.

class OpsRegister(APIView): 
    def post(self, request): 
        data = request.data
        serializer = OpsSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            
            serializer.save()  
            response = {'message': 'registered success', 'data': serializer.validated_data}
            return Response(response, status=status.HTTP_201_CREATED )
        return Response({'message': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class VerifyEmail(APIView):
    def get(self, request, token):
        try:
            user = User.objects.get(verification_token=token)

            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({'message': 'Email successfully verified'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Email already verified'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'message': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)



class OpsLogin(APIView): 
    def post(self, request): 
        data = request.data
        print(data)
        serializer = OpsLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            response = {'message': 'Login success', 'data': serializer.validated_data}
            return Response(response, status=status.HTTP_200_OK)
        return Response({'message': 'error', 'data': serializer.error_messages})




class ClientRegister(APIView): 
    def post(self, request): 
        data = request.data
        serializer = ClientSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            serializer.save()  
            response = {'message': 'registered success', 'data': serializer.validated_data}
            return Response(response, status=status.HTTP_201_CREATED )
        return Response({'message': 'error', 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class ClientLogin(APIView): 
    def post(self, request): 
        data = request.data
        print(data)
        serializer = ClientLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True): 
            return Response({'message': 'Login success', 'data': serializer.validated_data})
        return Response({'message': 'error', 'data': serializer.error_messages})