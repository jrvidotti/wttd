# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription

class SubscriptionDetailTest(TestCase):

    def setUp(self):
        s = Subscription.objects.create(name='Junior Vidotti', cpf='12345678901',
            email='jrvidotti@gmail.com', phone='65-92054852')
        self.resp = self.client.post('/inscricao/%d/' % s.pk)

    def test_get(self):
        'GET /incricao/1/ should return 200'
        self.assertEqual(200, self.resp.status_code)

    def test_template_used(self):
        'Uses template subscriptions_detail.html'
        self.assertTemplateUsed(self.resp, 'subscriptions/subscriptions_detail.html')

    def test_context(self):
        'Has Subscription data'
        s = self.resp.context['subscription']
        self.assertIsInstance(s, Subscription)

    def test_html(self):
        'Check if subscription data was rendered'
        self.assertContains(self.resp, 'Junior Vidotti')

class DetailNotFoundTest(TestCase):

    def test_not_found(self):
        'When subscription id doesnt exists, show 404'
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)

