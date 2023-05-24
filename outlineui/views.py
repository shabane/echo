from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from outline.models import Server, Channel, Link


def home(request):
    links = Link.objects.all()
    context = {
        'links': links,
    }
    return render(request, 'index.html', context)