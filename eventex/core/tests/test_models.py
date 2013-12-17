# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError
from eventex.core.models import Speaker, Contact


class SpeakerModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            description='Passionate software developer',
            url='http://henriquebastos.net',
            slug='henrique-bastos',
        )

    def test_create(self):
        """Test if object was saved"""
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        """Test object unicode representation"""
        self.assertEqual(u'Henrique Bastos', unicode(self.speaker))


class ContactModelTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            description='Passionate software developer',
            url='http://henriquebastos.net',
            slug='henrique-bastos',
        )
        self.email = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.phone = Contact.objects.create(speaker=self.speaker, kind='P', value='21-9999-0000')
        self.fax = Contact.objects.create(speaker=self.speaker, kind='F', value='21-1234-5678')

    def test_email(self):
        self.assertTrue(self.email.pk)

    def test_phone(self):
        self.assertTrue(self.phone.pk)

    def test_fax(self):
        self.assertTrue(self.fax.pk)

    def test_kind(self):
        contact = Contact(speaker=self.speaker, kind='A', value='21-1234-5678')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """Test object unicode representation"""
        self.assertEqual(u'henrique@bastos.net', unicode(self.email))