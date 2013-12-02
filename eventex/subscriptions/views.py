# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
    return render(request, 'subscriptions/subscriptions_form.html',
        {'form': SubscriptionForm()})