from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import action
from django.http import QueryDict
from django.db.models import Count
import jwt
from .serializers import *

class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        return Departamento.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                # Consultar si el departamento a crear existe previamente
                count_departamentos = Departamento.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_departamentos > 0:
                    return Response({
                        'detail': 'Este departamento ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                
                result = super().create(data, *args, **kwargs)
                return Response(result.data, HTTPStatus.CREATED)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            registro_actual = Departamento.objects.filter(id=request.data['id']).first()
            data = self.serializer_class(registro_actual, data=request.data)
            if data.is_valid(raise_exception=True):
                # Validar si el nuevo nombre no se encuentra registrado previamente
                count_departamentos = Departamento.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_departamentos > 0 and (registro_actual.nombre.casefold() != data.initial_data['nombre'].casefold()):
                    return Response({
                        'detail': 'Este departamento ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Departamento eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class MunicipioViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        return Municipio.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                # Consultar si el municipio a crear existe previamente
                count_municipios = Municipio.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_municipios > 0:
                    return Response({
                        'detail': 'Este municipio ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                
                result = super().create(data, *args, **kwargs)
                return Response(result.data, HTTPStatus.CREATED)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            registro_actual = Municipio.objects.filter(id=request.data['id']).first()
            data = self.serializer_class(registro_actual, data=request.data)
            if data.is_valid(raise_exception=True):
                # Validar si el nuevo nombre no se encuentra registrado previamente
                count_municipios = Municipio.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_municipios > 0 and (registro_actual.nombre.casefold() != data.initial_data['nombre'].casefold()):
                    return Response({
                        'detail': 'Este municipio ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Municipio eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class ComunaViewSet(viewsets.ModelViewSet):
    serializer_class = ComunaSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        return Comuna.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                # Consultar si la comuna a crear existe previamente
                count_comunas = Comuna.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_comunas > 0:
                    return Response({
                        'detail': 'Esta Comuna ya se encuentra registrada'
                    }, HTTPStatus.CONFLICT)
                
                result = super().create(data, *args, **kwargs)
                return Response(result.data, HTTPStatus.CREATED)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            registro_actual = Comuna.objects.filter(id=request.data['id']).first()
            data = self.serializer_class(registro_actual, data=request.data)
            if data.is_valid(raise_exception=True):
                # Validar si el nuevo nombre no se encuentra registrado previamente
                count_comunas = Comuna.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_comunas > 0 and (registro_actual.nombre.casefold() != data.initial_data['nombre'].casefold()):
                    return Response({
                        'detail': 'Esta comuna ya se encuentra registrada'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Comuna eliminada'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class BarrioViewSet(viewsets.ModelViewSet):
    serializer_class = BarrioSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        return Barrio.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                # Consultar si el barrio a crear existe previamente
                count_barrios = Barrio.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_barrios > 0:
                    return Response({
                        'detail': 'Este barrio ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                
                result = super().create(data, *args, **kwargs)
                return Response(result.data, HTTPStatus.CREATED)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            registro_actual = Barrio.objects.filter(id=request.data['id']).first()
            data = self.serializer_class(registro_actual, data=request.data)
            if data.is_valid(raise_exception=True):
                # Validar si el nuevo nombre no se encuentra registrado previamente
                count_barrios = Barrio.objects.filter(nombre__unaccent__iexact=request.data['nombre']).count()
                if count_barrios > 0 and (registro_actual.nombre.casefold() != data.initial_data['nombre'].casefold()):
                    return Response({
                        'detail': 'Este barrio ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Barrio eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class PuestoVotacionViewSet(viewsets.ModelViewSet):
    serializer_class = PuestoVotacionSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        # Validar rol
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('La sesión ha caducado')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        user_serializer_data = serializer.data

        # ADMIN = VISUALIZACIÓN COMPLETA
        if user_serializer_data['rol'] == 1:
            return PuestoVotacion.objects.all().order_by('nombre')
        # LIDER - LIMITAR A SU IDENTIFICADOR
        else:
            return PuestoVotacion.objects.filter(id_fk_usuario=user_serializer_data['id']).order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('La sesión ha caducado')

            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)
            user_serializer_data = serializer.data

            if isinstance(request.data, QueryDict):
                request.data._mutable = True
            request.data['id_fk_usuario'] = user_serializer_data['id']

            # SÓLO UN LIDER (ROL = 2) PUEDE REGISTRAR INFORMACIÓN DEL PUESTO DE VOTACIÓN
            if user_serializer_data['rol'] == 1:
                return Response({
                    'detail': 'El usuario no tiene permisos de escritura'
                }, HTTPStatus.UNAUTHORIZED)

            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                # Consultar si el puesto de votación a crear existe previamente
                count_puestos = PuestoVotacion.objects.filter(nombre__unaccent__iexact=request.data['nombre'], id_fk_municipio=request.data['id_fk_municipio']).count()
                if count_puestos > 0:
                    return Response({
                        'detail': 'Este puesto de votación ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                
                result = super().create(data, *args, **kwargs)
                return Response(result.data, HTTPStatus.CREATED)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            registro_actual = PuestoVotacion.objects.filter(id=request.data['id']).first()
            data = self.serializer_class(registro_actual, data=request.data)
            if data.is_valid(raise_exception=True):
                # Validar si el nuevo nombre no se encuentra registrado previamente
                count_puestos = PuestoVotacion.objects.filter(nombre__unaccent__iexact=request.data['nombre'], id_fk_municipio=request.data['id_fk_municipio']).count()
                if count_puestos > 0 and (registro_actual.nombre.casefold() != data.initial_data['nombre'].casefold()):
                    return Response({
                        'detail': 'Este puesto de votación ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Puesto de votación eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class VotanteViewSet(viewsets.ModelViewSet):
    serializer_class = VotanteSerializer

    def get_queryset(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('La sesión ha caducado')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        user_serializer_data = serializer.data

        if user_serializer_data['rol'] == 1:
            return Votante.objects.all()
        
        return Votante.objects.filter(id_fk_usuario=user_serializer_data['id']).order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('La sesión ha caducado')

            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)
            user_serializer_data = serializer.data

            # Validar rol
            if user_serializer_data == 1:
                return Response({
                    'detail': 'El usuario no tiene permisos de escritura'
                }, HTTPStatus.UNAUTHORIZED)
            
            # Registrar votante
            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                result = super().create(data, *args, **kwargs)
                # GET result
                votante = Votante.objects.filter(id=result.data['id']).first()
                Traza.objects.create(id_fk_usuario=user, id_fk_votante=votante)
                return Response(result.data, HTTPStatus.CREATED)

        except Exception as e:
            return Response({ 'detail': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            result = super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Votante eliminado',
            }, HTTPStatus.OK)
        except Exception as e:
            return Response({ 'detail': str(e) }, HTTPStatus.INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            token = self.request.COOKIES.get('token')

            if not token:
                raise AuthenticationFailed('La sesión ha caducado')

            try:
                payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            except jwt.ExpiredSignatureError:
                raise AuthenticationFailed('La sesión ha caducado')

            user = User.objects.filter(id=payload['id']).first()
            serializer = UserSerializer(user)
            user_serializer_data = serializer.data

            if user_serializer_data['rol'] == 1:
                return Response({
                    'detail': 'El usuario no tiene permisos de escritura'
                }, HTTPStatus.UNAUTHORIZED)

            registro_actual = Votante.objects.filter(id=request.data['id']).first()
            serializer = self.serializer_class(registro_actual, data=request.data)

            if serializer.is_valid(raise_exception=True):
                count_votantes = Votante.objects.filter(cedula=request.data['cedula']).count()
                if count_votantes > 0 and (registro_actual.cedula != serializer.initial_data['cedula']):
                    return Response({
                        'detail': 'Este votante ya se encuentra registrado'
                    }, HTTPStatus.CONFLICT)
                else:
                    result = super().update(request, *args, **kwargs)
                    return Response(result.data, HTTPStatus.OK)

        except Exception as e:
            return Response({ 'detail': str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def votantes_lider(self, request):

        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        lista_votantes = Votante.objects.filter(id_fk_usuario__rol=2).values('id_fk_usuario').annotate(total=Count('id_fk_usuario')).order_by('id_fk_usuario')
        data = []
        
        for item in lista_votantes:
            usuario = User.objects.filter(id=item['id_fk_usuario']).first()
            data.append({
                'nombre': f'{usuario.first_name} {usuario.last_name}',
                'usuario': usuario.email,
                'cantidad_votantes': item['total']
            })

        return Response(data, HTTPStatus.OK)

    @action(detail=False, methods=['get'])
    def votantes_general(self, request):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        count_votantes = Votante.objects.all().count()
        return Response({
            'detail': 'Cantidad de votantes en el sistema',
            'value': count_votantes
        })

    @action(detail=False, methods=['get'])
    def votantes_municipio(self, request):

        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        lista_votantes = Votante.objects.all().values('id_fk_puesto_votacion__id_fk_municipio').annotate(total=Count('id_fk_puesto_votacion__id_fk_municipio')).order_by('id_fk_puesto_votacion')
        data = []
        
        for item in lista_votantes:
            municipio = Municipio.objects.filter(id=item['id_fk_puesto_votacion__id_fk_municipio']).first()
            data.append({
                'id': municipio.id,
                'municipio': municipio.nombre,
                'cantidad_votantes': item['total']
            })

        return Response(data, HTTPStatus.OK)

    @action(detail=False, methods=['get'])
    def votantes_mesa(self, request):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        lista_votantes = Votante.objects.all().values('mesa').annotate(total=Count('mesa')).order_by('mesa')
        data = []

        for item in lista_votantes:
            data.append({
                'mesa': item['mesa'],
                'cantidad_votantes': item['total']
            })

        return Response(data, HTTPStatus.OK)

class TrazaViewSet(viewsets.ModelViewSet):
    serializer_class = TrazaSerializer

    def get_queryset(self):
        return super().get_queryset()
