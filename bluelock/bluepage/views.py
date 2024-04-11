from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView

from .models import Ai_tools
# def nigga(request):
#     items = Ai_tools.objects.all()
#     context = {
#         'items': items
#     }
#     return render(request, 'bluepage/Firs1t.html', context)

class Ai_tools_ai(ListView):
    model = Ai_tools
    template_name = 'bluepage/Firs1t.html'
    context_object_name = 'items'
# def index(request, id_my):
#     item = Ai_tools.objects.get(id=id_my)
#     context = {
#         'items': item
#     }
#     return render(request, 'bluepage/detail.html', context=context)

class Ai_tools_detail(DetailView):
    model = Ai_tools
    template_name = 'bluepage/detail.html'
    context_object_name = 'items'

def add_ai(request):
    if request.method == "POST":
        name = request.POST.get('name')
        seller = request.user
        about = request.POST.get('about')
        link_to = request.POST.get('link_to')
        data_time = request.POST.get('data_time')
        image = request.FILES['image']
        item = Ai_tools(name=name, about=about, link_to=link_to, data_time=data_time, image=image, seller=seller)
        item.save()
    return render(request,'bluepage/add.html')

def updateitem(request, id_my):
    item = Ai_tools.objects.get(id=id_my)
    context = {
        'items': item
    }
    if request.method == "POST":
        item.name = request.POST.get('name')
        item.seller = request.user
        item.about = request.POST.get('about')
        item.link_to = request.POST.get('link_to')
        item.data_time = request.POST.get('data_time')
        item.image = request.FILES.get('image', item.image)
        item.save()
        return redirect("/")
    return render(request,'bluepage/readd.html', context=context)


def deleteitem(request, id_my):
    item = Ai_tools.objects.get(id=id_my)
    context = {
        'items': item
    }
    if request.method == "POST":
        item.delete()
        return redirect("/")
    return render(request,'bluepage/del_ai.html', context=context)
