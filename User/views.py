from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import status
from .serializer import UserSerializer
from django.contrib.auth import authenticate
from django.contrib.auth import logout

# Create your views here.

class CreateUserView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class LoginUserView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        email = request.data["email"]
        password = request.data["password"]
        
        user  = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "id":user.id, "email":user.email}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    
    
class LogoutUserView(APIView):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    
    def post(self, request):
        try:
            request.user.auth_token.delete()
            logout(request)
            return Response({"message": "Logout successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"message": "Error in logout"}, status=status.HTTP_400_BAD_REQUEST)