# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _
from eventex.core.managers import KindContactManager, PeriodManager
from django.core.urlresolvers import reverse as r

class Speaker(models.Model):
    name = models.CharField(_(u'Nome'), max_length=255)
    description = models.TextField(_(u'Descrição'))
    url = models.URLField(_(u'URL'))
    slug = models.SlugField(_(u'Slug'))

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('core:speaker_detail', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'


class Contact(models.Model):
    KINDS = (
        ('E', 'E-mail'),
        ('P', 'Telefone'),
        ('F', 'Fax'),
    )

    speaker = models.ForeignKey('Speaker')
    kind = models.CharField(_(u'Tipo'), max_length=1, choices=KINDS)
    value = models.CharField(_(u'Valor'), max_length=255)

    objects = models.Manager()
    emails = KindContactManager(kind='E')
    phones = KindContactManager(kind='P')
    faxes = KindContactManager(kind='F')

    def __unicode__(self):
        return self.value

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'


class Talk(models.Model):
    title = models.CharField(_(u'Título'), max_length=200)
    description = models.TextField(_(u'Descrição da palestra'))
    start_time = models.TimeField(_(u'Horário'), blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name=_(u'palestrantes'))

    objects = PeriodManager()

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return '/palestras/%d/' % self.pk
        #return r('core:talk_detail', self.pk)

    class Meta:
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

