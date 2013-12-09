# coding: utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription
from django.core.urlresolvers import reverse as r

def subscribe(request):
    if request.method == 'POST':
        return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        obj = form.save()
        return HttpResponseRedirect(r('subscriptions:detail', args=[obj.pk]))
    else:
        return render(request, 'subscriptions/subscriptions_form.html',
            {'form': form})

def new(request):
    return render(request, 'subscriptions/subscriptions_form.html',
        {'form': SubscriptionForm()})

def detail(request, pk):
    s = get_object_or_404(Subscription, pk=pk)
    return render(request, 'subscriptions/subscriptions_detail.html', 
        {'subscription': s})
