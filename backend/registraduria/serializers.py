from rest_framework import serializers
from .models import *
from rest_flex_fields import FlexFieldsModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'rol']
        extra_kwargs = {
            'password': { 'write_only': True }
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class DepartamentoSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MunicipioSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'
        expandable_fields = {
            'id_fk_departamento': DepartamentoSerializer
        }

class ComunaSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'
        expandable_fields = {
            'id_fk_municipio': MunicipioSerializer
        }

class BarrioSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'
        expandable_fields = {
            'id_fk_comuna': ComunaSerializer
        }

class PuestoVotacionSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = PuestoVotacion
        fields = '__all__'
        expandable_fields = {
            'id_fk_municipio': MunicipioSerializer
        }

class VotanteSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'
        expandable_fields = {
            'id_fk_usuario': UserSerializer,
            'id_fk_barrio': BarrioSerializer,
            'id_fk_puesto_votacion': PuestoVotacionSerializer
        }

class TrazaSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Traza
        fields = '__all__'
        expandable_fields = {
            'id_fk_usuario': UserSerializer,
            'id_fk_votante': VotanteSerializer,
        }