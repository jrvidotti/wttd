# coding: utf-8
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Subscription(models.Model):
    name = models.CharField(_('nome'), max_length=100)
    cpf = models.CharField(_('CPF'), max_length=11, unique=True)
    email = models.EmailField(_('e-mail'), unique=True)
    phone = models.CharField(_('telefone'), max_length=20, blank=True)
    created_at = models.DateTimeField(_(u'data da criação'), auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = _(u'incrição')
        verbose_name_plural = _(u'incrições')

    def __unicode__(self):
        return self.name