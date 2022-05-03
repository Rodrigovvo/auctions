import re

from django.db import models

from validate_docbr import CPF, CNPJ

from apps.base.models import AuditModel


class Person(AuditModel):
    """Base Model to create users"""

    name    = models.CharField(verbose_name='Nome', max_length=128)
    about   = models.TextField(verbose_name='Sobre', blank=True, null=True)
    doc     = models.CharField(verbose_name='Documento de Identificação', max_length=18, unique=True)
    active  = models.BooleanField(verbose_name='Ativo ?', default=False)
    site    = models.URLField(verbose_name='Site', max_length=200, blank=True, null=True)
    
    class Meta:
        unique_together = ['name', 'doc']
    
    def __str__(self) -> str:
        return f'Pessoa: {self.name}'

    @classmethod
    def validate_doc(kls, doc:str) -> bool:
        """ Receive a doc and verify if is a valid doc 

        :param doc: the identification doc
        :type doc: str
        :return: True if a valid doc or False if else.
        :rtype: bool
        """
        is_valid = False
        if doc.isdigit():
            if len(doc) < 14:
                is_valid = kls.validate_cpf(doc)
            else:
                is_valid = kls.validate_cnpj(doc)
        else:     
            if len(doc) <= 14:
                is_valid = kls.validate_cpf(doc)
            else:
                is_valid = kls.validate_cnpj(doc)
        return is_valid

    @classmethod
    def validate_cpf(kls, cpf:str) -> bool:    
        """ Validate the CPF, for lenght and for verifies digits.
        
        :param cpf: (str) Parâmetro contendo o CPF
        :returns: (bool) Retorna True se o CPF for válido e False se inválido
        """
        valid_cpf = CPF()
        return valid_cpf.validate(cpf)
        
    @classmethod
    def validate_cnpj(kls, cnpj:str) -> bool:
        """ Validate the CNPJ, for lenght and for verifies digits.
        
        :param cnpj: (str) Parâmetro contendo o número do CNPJ
        :returns: (bool) Retorna True se o CNPJ for válido e False se inválido
        """
        valid_cnpj = CNPJ()
        return valid_cnpj.validate(cnpj)

    def save(self, *args, **kwargs) -> None:
        """Save the current instance. Save the numbers of doc."""
        self.doc = ''.join(list(filter(lambda x : x.isdigit(), self.doc)))
        return super().save(*args, **kwargs)


class Enterprise(Person):
    """ Model for enterprises """

    def __str__(self) -> str:
        return f'Empresa: {self.name} - {self.doc}'


class Client(Person):
    """ Model for clients """

    def __str__(self) -> str:
        return f'Cliente: {self.name}'
