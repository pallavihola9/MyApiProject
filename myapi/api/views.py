from django.shortcuts import render
from .models import *
from  .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
# Generate Token Manually
def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class RegisterUserPost(APIView):
    def post(self, request, format=None):
        serializer = UserDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


class UserDataGet(APIView):
    def get(self,request,format=None):
        userdata = RegisterUser.objects.all()
        serializer = UserDataSerializer(userdata,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

class UserDataUpdateDelete(APIView):
     def put(self,request,pk):
        userdata = RegisterUser.objects.get(pk=pk)
        serializer = UserDataSerializer(userdata,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
     def delete(self,request,pk):
        userdata = RegisterUser.objects.get(pk=pk)
        userdata.delete()
        return Response({"message": "deleted successfully."},status=status.HTTP_204_NO_CONTENT)    


