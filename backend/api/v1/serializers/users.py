from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import Client, Enterprise, Person


class PersonSerializer(serializers.ModelSerializer):
    """ Serializer for Person """

    class Meta:
        model = Person
        exclude = ('created_at', 'modified_at')

    def validate_doc(self, value):
        if not Person.validate_doc(value):
            raise ValidationError('O documento informado não é válido.')
        return value 


class EnterpriseSerializer(PersonSerializer):
    """ Serializer for enterprise """
    
    class Meta:
        model = Enterprise
        exclude = ('created_at', 'modified_at')


class ClientSerializer(PersonSerializer):
    """ Serializer for enterprise """
    
    class Meta:
        model = Client
        exclude = ('created_at', 'modified_at')
        