# coding: utf-8
from django.test import TestCase
from eventex.core.models import Talk
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):

    def setUp(self):
        self.talk = Talk.objects.create(
            title=u'Introdução ao Django',
            description=u'Descrição da palestra',
            start_time=u'10:00')

    def test_create(self):
        self.assertEqual(1, self.talk.pk)

    def test_unicode(self):
        self.assertEqual(u'Introdução ao Django', unicode(self.talk))

    def test_speakers(self):
        self.talk.speakers.create(name='Henrique Bastos',
                                  slug='henrique-bastos',
                                  url='http://henriquebastos.net')
        self.assertEqual(1, self.talk.speakers.count())

    def test_period_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)


class PeriodManagerTest(TestCase):

    def setUp(self):
        Talk.objects.create(title=u'Morning talk', start_time=u'10:00')
        Talk.objects.create(title=u'Afternoon talk', start_time=u'13:00')

    def test_morning(self):
        self.assertQuerysetEqual(
            Talk.objects.at_morning(),
            [u'Morning talk'],
            lambda t: t.title
        )

    def test_afternoon(self):
        self.assertQuerysetEqual(
            Talk.objects.at_afternoon(),
            [u'Afternoon talk'],
            lambda t: t.title
        )
