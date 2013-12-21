# coding: utf-8
from django.test import TestCase
from django.core.urlresolvers import reverse as r
from eventex.core.models import Speaker, Talk


class TalkListTest(TestCase):

    def setUp(self):
        s = Speaker.objects.create(name='Henrique Bastos',
                                   slug='henrique-bastos',
                                   url='http://henriquebastos.net',
                                   description='Passionate software developer!')
        t1 = Talk.objects.create(description='Descrição da palestra',
                                 title='Título da palestra',
                                 start_time='10:00')
        t2 = Talk.objects.create(description='Descrição da palestra',
                                 title='Título da palestra',
                                 start_time='13:00')
        t1.speakers.add(s)
        t2.speakers.add(s)
        self.resp = self.client.get(r('core:talk_list'))

    def test_get(self):
        """GET / must return status code 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Home must use template indx.html"""
        self.assertTemplateUsed(self.resp, 'core/talk_list.html')

    def test_html(self):
        """HTML must contain data"""
        contents = ((u'Título da palestra', 2),
                    (u'10:00', 1),
                    (u'13:00', 1),
                    (u'/palestras/1/', 1),
                    (u'/palestras/2/', 1),
                    (u'/palestrantes/henrique-bastos/', 2),
                    (u'Henrique Bastos', 2),
                    (u'Descrição da palestra', 2))

        for content in contents:
            self.assertContains(self.resp, content[0], content[1])

    def test_morning_talks_in_context(self):
        self.assertIn('morning_talks', self.resp.context)

    def test_afternoon_talks_in_context(self):
        self.assertIn('afternoon_talks', self.resp.context)
