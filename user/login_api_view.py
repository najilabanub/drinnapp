from rest_framework.views import APIiew
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import status
from .models import User

class LoginView(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email,password=password)


        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'usertype': user.usertype,
                }
            )
        else:
            return Response({"error:Invalid Credentials"},status = status.HTTP_401_UNAUTHORIZED)