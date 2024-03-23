from django.shortcuts import render, HttpResponse
from .models import Ai_tools
def nigga(request):
    items = Ai_tools.objects.all()
    context = {
        'items': items
    }
    return render(request, 'bluepage/Firs1t.html', context)


def index(request, id_my):
    item = Ai_tools.objects.get(id=id_my)
    context = {
        'items': item
    }
    return render(request, 'bluepage/detail.html', context=context)