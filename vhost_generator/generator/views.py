from django.shortcuts import render
from .forms import *
# Create your views here.


def generate(request):
    form = VhostForm()
    return render(request, 'generator/form.html', locals())


def results(request):
    form = VhostForm(request.POST)
    if form.is_valid():
        ssenv = form.cleaned_data['ssenv']
        path = form.cleaned_data['path']
        project = form.cleaned_data['project']
    return render(request, 'generator/results.html', locals())
