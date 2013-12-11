# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm

class SubscriptionFormTest(TestCase):

    def test_form_has_fields(self):
        'Form must have 4 fields'
        form = SubscriptionForm()
        self.assertItemsEqual(['name', 'cpf', 'email', 'phone'], form.fields)

    def test_email_is_optional(self):
        'Email is optional'
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_email_or_phone_was_informed(self):
        'Must inform email or phone number'
        form = self.make_validated_form(email='', phone='')
        self.assertIn('__all__', form.errors)

    def test_name_is_capitalized(self):
        'Given name filled not capitalized'
        form = self.make_validated_form(name='JUNIOR vidotti')

        'When the form is validated'
        form.is_valid()

        'Then the name is cleaned capitalized'
        self.assertEqual('Junior Vidotti', form.cleaned_data['name'])

    def test_name_is_capitalized_2(self):
        'Given name filled not capitalized'
        form = self.make_validated_form(name='JUNIOR vidotti da silva')

        'When the form is validated'
        form.is_valid()

        'Then the name is cleaned capitalized'
        self.assertEqual('Junior Vidotti da Silva', form.cleaned_data['name'])

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


