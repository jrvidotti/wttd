# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def test_cpf_is_digit(self):
        'Given CPF filled in subscription form was not digits'
        form = self.make_validated_form(cpf='ABCD5678901')

        'When the form is validated'
        form.is_valid()

        'Then then form must return errors in CPF field'
        self.assertItemsEqual(['cpf'], form.errors)

    def test_cpf_has_11_digits(self):
        'Given CPF filled in subscription form has not exactly 11 digits'
        form = self.make_validated_form(cpf='1234')

        'When the form is validated'
        form.is_valid()

        'Then then form must return errors in CPF field'
        self.assertItemsEqual(['cpf'], form.errors)

    def make_validated_form(self, **kwargs):
        data = dict(name='Junior Vidotti', email='jrvidotti@gmail.com',
                    cpf='12345678901', phone='65-9999-9999')
        data.update(kwargs)
        form = SubscriptionForm(data)
        return form
