
from django.db import IntegrityError
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.exceptions import  NotFound, NotAcceptable
from rest_framework.response import Response

from api.v1.serializers.users import ClientSerializer, EnterpriseSerializer, PersonSerializer
from apps.users.models import Client, Enterprise, Person


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.order_by('-modified_at')
    serializer_class = PersonSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        try: 
            response = super().create(request, *args, **kwargs)
        except IntegrityError:
            raise NotAcceptable('Já existe uma pessoa com mesmo nome e documento.')
    

    @action(detail=False, methods=['get'], name='get-persons',
    url_path='get-persons', url_name='get-persons')
    def get_active_persons(self, request):
        """ 
        Action to returns serializer for active People
        
        :returns: (Response)
        """
        persons = Person.objects.filter(active=True)
        serializer_context = {
            'request': request,
        }

        serializer = self.serializer_class(
            persons, many=True, context=serializer_context)
        return Response(serializer.data)


class EnterpriseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Enterprise.objects.filter(active=True).order_by('-modified_at')
    serializer_class = EnterpriseSerializer
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.active = False
            instance.save()
        else:
            raise NotFound('Empresa não localizada.')
        return Response(status=status.HTTP_204_NO_CONTENT, content_type='json')


class ClientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows offers to be viewed or edited.
    """
    queryset = Client.objects.filter(active=True).order_by('modified_at')
    serializer_class = ClientSerializer
    permission_classes = []

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance:
            instance.active = False
            instance.save()
        else:
            raise NotFound('Empresa não localizada.')
        return Response(status=status.HTTP_204_NO_CONTENT, content_type='json')
