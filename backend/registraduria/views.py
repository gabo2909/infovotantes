from http import HTTPStatus
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed

from .serializers import UserSerializer
from .models import User

import jwt, datetime

# Create your views here.
class RegistrarUsuarioView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, HTTPStatus.CREATED)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        # Validar que el usuario se encuentre registrado
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Usuario no encontrado')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Credenciales inválidas')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(
            key='token',
            value=token,
            httponly=True
        )
        response.data = {
            'token': token
        }
        response.status_code = HTTPStatus.OK

        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('La sesión ha caducado')
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'detail': 'Sesión finalizada'
        }
        response.status_code = HTTPStatus.OK

        return response