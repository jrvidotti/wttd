# coding: utf-8
from django.test import TestCase
from eventex.subscriptions.models import Subscription
from datetime import datetime
from django.db import IntegrityError

class SubscriptionTest(TestCase):

    def setUp(self):
        self.obj = Subscription(
            name='Junior Vidotti',
            cpf='12345678901',
            email='jrvidotti@gmail.com',
            phone='65-92054852',
            )

    def test_create(self):
        'Test if saves'
        self.obj.save()
        self.assertEqual(1, self.obj.pk)

    def test_has_created_at(self):
        'Test if has create_at'
        self.obj.save()
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_unicode(self):
        self.assertEqual(u'Junior Vidotti', unicode(self.obj))


class SubscriptionUniqueTest(TestCase):

    def setUp(self):
        Subscription.objects.create(
            name='Junior Vidotti', cpf='12345678901',
            email='jrvidotti@gmail.com', phone='65-92054852')

    def test_cpf_unique(self):
        'CPF must be unique'
        s = Subscription(
            name='Junior Vidotti', cpf='12345678901',
            email='outroemail@gmail.com', phone='65-92054852')
        self.assertRaises(IntegrityError, s.save)

    def test_email_unique(self):
        'Email must be unique'
        s = Subscription(
            name='Junior Vidotti', cpf='11111111100',
            email='jrvidotti@gmail.com', phone='65-92054852')
        self.assertRaises(IntegrityError, s.save)
