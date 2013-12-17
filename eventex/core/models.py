# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Speaker(models.Model):
    name = models.CharField(_(u'Nome'), max_length=255)
    description = models.TextField(_(u'Descrição'))
    url = models.URLField(_(u'URL'))
    slug = models.SlugField(_(u'Slug'))

    def __unicode__(self):
        return self.name


class Contact(models.Model):
    KINDS = (
        ('E', 'E-mail'),
        ('P', 'Telefone'),
        ('F', 'Fax'),
    )

    speaker = models.ForeignKey('Speaker')
    kind = models.CharField(_(u'Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_(u'Valor'), max_length=255)

    def __unicode__(self):
        return self.value

