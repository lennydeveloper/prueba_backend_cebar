from http import HTTPStatus
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.decorators import action
from django.http import QueryDict
from django.db.models import Count
import jwt
from .serializers import *
from .models import User

class DepartamentoViewSet(viewsets.ModelViewSet):
    serializer_class = DepartamentoSerializer

    def obtener_token(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

    def get_queryset(self):
        self.obtener_token()
        return Departamento.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            self.obtener_token()

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
            self.obtener_token()

            registro_actual = Departamento.objects.get(id=request.data['id'])
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
            self.obtener_token()

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Departamento eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class MunicipioViewSet(viewsets.ModelViewSet):
    serializer_class = MunicipioSerializer

    def obtener_token(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

    def get_queryset(self):
        self.obtener_token()

        return Municipio.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            self.obtener_token()

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
            self.obtener_token()

            registro_actual = Municipio.objects.get(id=request.data['id'])
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
            self.obtener_token()

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Municipio eliminado'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class ComunaViewSet(viewsets.ModelViewSet):
    serializer_class = ComunaSerializer

    def obtener_token(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

    def get_queryset(self):
        self.obtener_token()

        return Comuna.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            self.obtener_token()

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
            self.obtener_token()

            registro_actual = Comuna.objects.get(id=request.data['id'])
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
            self.obtener_token()

            super().destroy(request, *args, **kwargs)
            return Response({
                'detail': 'Comuna eliminada'
            }, HTTPStatus.OK)
        except Exception as e:
            return Response(e, HTTPStatus.INTERNAL_SERVER_ERROR)


class BarrioViewSet(viewsets.ModelViewSet):
    serializer_class = BarrioSerializer

    def obtener_token(self):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

    def get_queryset(self):
        self.obtener_token()

        return Barrio.objects.all().order_by('nombre')

    def create(self, request, *args, **kwargs):
        try:
            self.obtener_token()

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
            self.obtener_token()

            registro_actual = Barrio.objects.get(id=request.data['id'])
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
            self.obtener_token()

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

        user = User.objects.get(id=payload['id'])
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

            user = User.objects.get(id=payload['id'])
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

            registro_actual = PuestoVotacion.objects.get(id=request.data['id'])
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

        user = User.objects.get(id=payload['id'])
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

            user = User.objects.get(id=payload['id'])
            serializer = UserSerializer(user)
            user_serializer_data = serializer.data

            # Validar rol
            if user_serializer_data['rol'] == 1:
                return Response({
                    'detail': 'El usuario no tiene permisos de escritura'
                }, HTTPStatus.UNAUTHORIZED)
            
            # Registrar votante
            data = self.serializer_class(data=request.data)
            if data.is_valid(raise_exception=True):
                result = super().create(data, *args, **kwargs)
                # GET result
                votante = Votante.objects.get(id=result.data['id'])
                desc_traza = 'Votante registrado exitosamente'
                Traza.objects.create(id_fk_usuario=user, id_fk_votante=votante, descripcion=desc_traza)
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

            user = User.objects.get(id=payload['id'])
            serializer = UserSerializer(user)
            user_serializer_data = serializer.data

            if user_serializer_data['rol'] == 1:
                return Response({
                    'detail': 'El usuario no tiene permisos de escritura'
                }, HTTPStatus.UNAUTHORIZED)

            registro_actual = Votante.objects.get(id=request.data['id'])
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

    # Cantidad total de votantes inscritos por líder
    @action(detail=False, methods=['get'])
    def votantes_lider(self, request):

        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        data = []
        lista_lideres = User.objects.filter(rol=2).order_by('id')

        for lider in lista_lideres:
            count_votantes = Votante.objects.filter(id_fk_usuario=lider.id).count()
            data.append({
                'nombre': f'{lider.first_name} {lider.last_name}',
                'usuario': lider.email,
                'votantes_inscritos': count_votantes
            })

        return Response(data, HTTPStatus.OK)

    # Cantidad total de votantes en el sistema
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

    # Cantidad total de votantes inscritos por municipio
    @action(detail=False, methods=['get'])
    def votantes_municipio(self, request):

        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        data = []
        lista_municipios = Municipio.objects.all().order_by('id')

        for municipio in lista_municipios:
            count_votantes = Votante.objects.filter(id_fk_puesto_votacion__id_fk_municipio=municipio.id).count()
            data.append({
                'id': municipio.id,
                'municipio': municipio.nombre,
                'cantidad_votantes': count_votantes
            })

        return Response(data, HTTPStatus.OK)

    # Cantidad total de votantes inscritos por mesa de votación
    @action(detail=False, methods=['get'])
    def votantes_mesa(self, request):
        token = self.request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed('La sesión ha caducado')

        data = []
        lista_mesas = Votante.objects.order_by('mesa').distinct('mesa')

        for item in lista_mesas:
            count_mesas = Votante.objects.filter(mesa=item.mesa).count()
            data.append({
                'mesa': item.mesa,
                'cantidad_votantes': count_mesas
            })

        return Response(data, HTTPStatus.OK)

class TrazaViewSet(viewsets.ModelViewSet):
    serializer_class = TrazaSerializer

    def get_queryset(self):
        return super().get_queryset()
