# coding: utf-8
from django.test import TestCase
from mock import Mock
from eventex.subscriptions.admin import SubscriptionAdmin, Subscription, admin

class MarkAsPaidTest(TestCase):

    def setUp(self):
        'Given a SubscriptionAdmin ModelAdmin'
        self.model_admin = SubscriptionAdmin(Subscription, admin.site)

        'And a subscription'
        Subscription.objects.create(name='Junior Vidotti', cpf='12345678901',
                                    email='jrvidotti@gmail.com')

    def test_has_action(self):
        'Then must exist a mark_as_paid action'
        self.assertIn('mark_as_paid', self.model_admin.actions)

    def test_mark_all(self):
        'When I mark all subscriptions'
        queryset = Subscription.objects.all()

        'And execute the mark_as_paid action'
        fake_request = Mock()
        self.model_admin.mark_as_paid(fake_request, queryset)

        'Then I must see 1 paid subscription'
        self.assertEqual(1, Subscription.objects.filter(paid=True).count())
