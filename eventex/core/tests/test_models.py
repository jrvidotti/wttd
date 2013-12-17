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

    def test_email(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='P', value='21-9999-0000')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(speaker=self.speaker, kind='F', value='21-1234-5678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        contact = Contact(speaker=self.speaker, kind='A', value='21-1234-5678')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        """Test object unicode representation"""
        contact = Contact.objects.create(speaker=self.speaker, kind='E', value='henrique@bastos.net')
        self.assertEqual(u'henrique@bastos.net', unicode(contact))
