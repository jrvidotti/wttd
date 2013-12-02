# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription

class SubscribeTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/inscricao/')

    def test_get(self):
        'GET /inscricao/ must return status code 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        'Response should be a rendered template'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_form.html')

    def test_html(self):
        'HTML must contain input controls'
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 6)
        self.assertContains(self.resp, 'type="text"', 3)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf(self):
        'HTML must have CSRF token'
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_form(self):
        'Context must have the subscription form'
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

class SubscribePostTest(TestCase):

    def setUp(self):
        self.data = dict(name='Junior Vidotti', cpf='12345678901',
            email='jrvidotti@gmail.com', phone='65-92054852')
        self.resp = self.client.post('/inscricao/', self.data)

    def test_redirect(self):
        'Valid POST should redirect to /inscricao/1/'
        self.assertEqual(302, self.resp.status_code)

    def test_save(self):
        'Test if subscription exists'
        self.assertTrue(Subscription.objects.exists())


class SubscribeErrorTest(TestCase):

    def setUp(self):
        self.data = dict(name='Junior Vidotti', cpf='123456789012',  # CPF com 12 digitos
            email='jrvidotti@gmail.com', phone='65-92054852')
        self.resp = self.client.post('/inscricao/', self.data)

    def test_error(self):
        'Invalid POST should not redirect'
        self.assertEqual(200, self.resp.status_code)

    def test_form_errors(self):
        'Form must contain errors'
        self.assertTrue(self.resp.context['form'].errors)

    def test_dont_save(self):
        'Do not save data'
        self.assertFalse(Subscription.objects.exists())


