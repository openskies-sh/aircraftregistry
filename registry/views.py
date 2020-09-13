import datetime
import json

from datetime import datetime
from django.core.exceptions import PermissionDenied
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.utils import translation
from django.views.generic import TemplateView
from rest_framework import generics, mixins, status, viewsets
from rest_framework.authentication import (SessionAuthentication,
                                           TokenAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from registry.models import Activity, Authorization, Contact, Operator, Aircraft, Pilot, Test, TestValidity
from registry.serializers import (ContactSerializer, ContactDetailSerializer, OperatorSerializer, PilotSerializer, PilotDetailSerializer,
                                  PrivilegedContactSerializer, PrivilegedPilotDetailSerializer, 
                                  PrivilegedOperatorSerializer, AircraftSerializer, AircraftDetailSerializer, AircraftESNSerializer)
from django.http import JsonResponse
from rest_framework.decorators import api_view
from six.moves.urllib import request as req
from functools import wraps
import os
import jwt
from django.core.exceptions import PermissionDenied
from functools import wraps
from django.conf import settings
from django.utils.decorators import method_decorator
from cryptography.x509 import load_pem_x509_certificate
from cryptography.hazmat.backends import default_backend

# Create your views here.


def requires_scopes(required_scopes):
    """Determines if the required scope is present in the access token
    Args:
        required_scopes (list): The scopes required to access the resource
    """
    def require_scope(f):
        @wraps(f)
        def decorated(*args, **kwargs):           
            if settings.SECURE_API_ENDPOINTS: 
                request = args[0]
                auth = request.META.get("HTTP_AUTHORIZATION", None)
                
                if auth:
                    parts = auth.split()
                    token = parts[1]            
                else:             
                    response = JsonResponse({'detail': 'Authentication credentials were not provided'})
                    response.status_code = 401
                    return response

                AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
                API_IDENTIFIER = os.environ.get('API_IDENTIFIER')
                jsonurl = req.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
                jwks = json.loads(jsonurl.read())
                cert = '-----BEGIN CERTIFICATE-----\n' + \
                    jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
                certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
                public_key = certificate.public_key()
                try:
                    decoded = jwt.decode(token, public_key, audience=API_IDENTIFIER, algorithms=['RS256'])
                except jwt.ExpiredSignatureError as es: 
                    response = JsonResponse({'detail': 'Token Signature has expired'})
                    response.status_code = 401
                    return response
                except jwt.InvalidAudienceError as es: 
                    response = JsonResponse({'detail': 'Invalid audience in token'})
                    response.status_code = 401
                    return response
                
                except jwt.InvalidIssuerError as es: 
                    response = JsonResponse({'detail': 'Invalid issuer for token'})
                    response.status_code = 401
                    return response

                except jwt.InvalidSignatureError as es: 
                    response = JsonResponse({'detail': 'Invalid signature in token'})
                    response.status_code = 401
                    return response
                except Exception as e: 
                    response = JsonResponse({'detail': 'Invalid token'})
                    response.status_code = 401
                    return response

                

                if decoded.get("scope"):
                    token_scopes = decoded["scope"].split()
                    token_scopes_set = set(token_scopes)                
                    if set(required_scopes).issubset(token_scopes_set):
                        return f(*args, **kwargs)
                response = JsonResponse({'message': 'You don\'t have access to this resource'})
                response.status_code = 403
                return response
            else:
                return f(*args, **kwargs)
        return decorated

    return require_scope


@method_decorator(requires_scopes(['registry.read.operator']), name='dispatch')
class OperatorList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    """
    List all operators, or create a new operator.
    """

    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(requires_scopes(['registry.read.operator_detail']), name='dispatch')
class OperatorDetail(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    """
    Retrieve, update or delete a Operator instance.
    """
    # authentication_classes = (SessionAuthentication,TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@method_decorator(requires_scopes(['registry.read.aircraft']), name='dispatch')
class AircraftList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    """
    List all aircrafts in the database
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(requires_scopes(['registry.read.aircraft_detail']), name='dispatch')
class AircraftDetail(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    """
    Retrieve, update or delete a Aircraft instance.
    """
    # authentication_classes = (SessionAuthentication,TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get_Aircraft(self, pk):
        try:
            a = Aircraft.objects.get(id=pk)
        except Aircraft.DoesNotExist:
            raise Http404
        else:
            return a

    def get(self, request, pk, format=None):
        aircraft = self.get_Aircraft(pk)
        serializer = AircraftSerializer(aircraft)
        return Response(serializer.data)



@method_decorator(requires_scopes(['registry.read.aircraft_detail.privileged']), name='dispatch')
class AircraftDetailPrivileged(mixins.RetrieveModelMixin,
                     generics.GenericAPIView):
    """
    Retrieve, update or delete a Aircraft instance.
    """
    # authentication_classes = (SessionAuthentication,TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    def get_Aircraft(self, pk):
        try:
            a = Aircraft.objects.get(id=pk)
        except Aircraft.DoesNotExist:
            raise Http404
        else:
            return a

    def get(self, request, pk, format=None):
        aircraft = self.get_Aircraft(pk)
        serializer = AircraftDetailSerializer(aircraft)
        return Response(serializer.data)


@method_decorator(requires_scopes(['registry.read.operator_detail.privileged']), name='dispatch')
class OperatorDetailPrivileged(mixins.RetrieveModelMixin,
                               generics.GenericAPIView):
    """
    Retrieve, update or delete a Operator instance.
    """

    queryset = Operator.objects.all()
    serializer_class = PrivilegedOperatorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(requires_scopes(['registry.read.operator_aircraft']), name='dispatch')
class OperatorAircraft(mixins.RetrieveModelMixin,
                       generics.GenericAPIView):
    """
    Retrieve, update or delete a Operator instance.
    """

    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

    def get_Aircraft(self, pk):
        try:
            o = Operator.objects.get(id=pk)
        except Operator.DoesNotExist:
            raise Http404
        else:
            return Aircraft.objects.filter(operator=o)

    def get(self, request, pk, format=None):
        aircraft = self.get_Aircraft(pk)
        serializer = AircraftSerializer(aircraft, many=True)

        return Response(serializer.data)


@method_decorator(requires_scopes(['registry.read.aircraft.privileged']), name='dispatch')
class AircraftESNDetails(mixins.RetrieveModelMixin,
                         generics.GenericAPIView):

    queryset = Aircraft.objects.all()
    serializer_class = AircraftESNSerializer
    lookup_field = 'esn'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(requires_scopes(['registry.read.contact']), name='dispatch')
class ContactList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    """
    List all contacts in the database
    """

    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

@method_decorator(requires_scopes(['registry.read.contact_detail']), name='dispatch')
class ContactDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, update or delete a Contact instance.
    """

    queryset = Contact.objects.all()
    serializer_class = ContactDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@method_decorator(requires_scopes(['registry.read.contact_detail.privileged']), name='dispatch')
class ContactDetailPrivileged(mixins.RetrieveModelMixin,
                              generics.GenericAPIView):
    """
    Retrieve, update or delete a Contact instance.
    """

    queryset = Contact.objects.all()
    serializer_class = PrivilegedContactSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

@method_decorator(requires_scopes(['registry.read.pilot']), name='dispatch')
class PilotList(mixins.ListModelMixin,
                generics.GenericAPIView):
    """
    List all pilots in the database
    """
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


@method_decorator(requires_scopes(['registry.read.pilot_detail']), name='dispatch')
class PilotDetail(mixins.RetrieveModelMixin,
                  generics.GenericAPIView):
    """
    Retrieve, update or delete a Pilot instance.
    """
    # authentication_classes = (SessionAuthentication,TokenAuthentication)
    # permission_classes = (IsAuthenticated,)

    queryset = Pilot.objects.all()
    serializer_class = PilotDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        

@method_decorator(requires_scopes(['registry.read.pilot_detail.privileged']), name='dispatch')
class PilotDetailPrivileged(mixins.RetrieveModelMixin,
                            generics.GenericAPIView):
    """
    Retrieve, update or delete a Pilot instance.
    """

    queryset = Pilot.objects.all()
    serializer_class = PrivilegedPilotDetailSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = 'registry/index.html'


class APIView(TemplateView):
    template_name = 'registry/api.html'
