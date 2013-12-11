# coding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from eventex.subscriptions.models import Subscription

def CPFValidator(value):
    if not value.isdigit():
        raise ValidationError(_(u'CPF deve conter apenas números'))

    if len(value) != 11:
        raise ValidationError(_(u'CPF deve ter 11 números'))

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        exclude = ('paid',)

    def __init__(self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)

        self.fields['cpf'].validators.append(CPFValidator)

    def clean_name(self):
        def capitalize(word):
            word = word.capitalize()
            if word in ['De', 'Da', 'Dos', 'Das']:
                word = word.lower()
            return word
            
        name = self.cleaned_data['name']
        words = map(lambda w: capitalize(w), name.split())
        capitalized_name = ' '.join(words)
        return capitalized_name
        