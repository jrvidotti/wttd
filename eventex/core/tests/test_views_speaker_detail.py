# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker


class SpeakerDetailTest(TestCase):

    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            description='Passionate software developer',
            url='http://henriquebastos.net',
            slug='henrique-bastos',
        )
        url = r('core:speaker_detail', kwargs={'slug': 'henrique-bastos'})
        self.resp = self.client.get(url)

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Home must use template index.html"""
        self.assertTemplateUsed(self.resp, 'core/speaker_detail.html')

    def test_html(self):
        """HTML must contain data"""
        self.assertContains(self.resp, 'Henrique Bastos')
        self.assertContains(self.resp, 'Passionate software developer')
        self.assertContains(self.resp, 'http://henriquebastos.net')

    def test_context(self):
        """Speaker object must be in context"""
        speaker = self.resp.context['speaker']
        self.assertIsInstance(speaker, Speaker)


class SpeakerDetailNotFound(TestCase):

    def setUp(self):
        url = r('core:speaker_detail', kwargs={'slug': 'john-doe'})
        self.resp = self.client.get(url)

    def test_404(self):
        self.assertEqual(404, self.resp.status_code)
