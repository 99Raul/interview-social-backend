from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegistrationAPIView(APIView):
    
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # This method will return the serialized representations of new refresh
            #  and access tokens for the given user.
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
            return Response(res, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer






# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import permissions
# from django.contrib.auth import get_user_model
# # from django.conf import settings
# User = get_user_model()

# class SignUpView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request, format=None):
#         data = self.request.data 

#         name = data['name']
#         email = data['email']
#         password = data['password']
#         password2 = data['password2']


#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 return Response({'error': 'Email already exists'})
            
#             else:
#                 if len(password) < 6:
#                     return Response({'password': 'Password must be at least 6 characters'})
#                 else:
#                     user = User.objects.create_user(email=email, password=password, name=name)

#                     user.save()
#                     return Response({'success': 'User created successfully'})

#         else:
#             return Response({'error': 'Passwords do not match'})
