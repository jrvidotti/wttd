# coding: utf-8
from django.shortcuts import render
from django.http import HttpResponseRedirect
from eventex.subscriptions.forms import SubscriptionForm

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return HttpResponseRedirect('/inscricao/%d/' % obj.pk)
    else:
        return render(request, 'subscriptions/subscriptions_form.html',
            {'form': form})

def new(request):
    return render(request, 'subscriptions/subscriptions_form.html',
        {'form': SubscriptionForm()})