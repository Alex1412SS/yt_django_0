from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from .models import Ai_tools
def nigga(request):
    page_obj =items = Ai_tools.objects.all()
    item_name = request.GET.get('search')
    if item_name != '' and item_name is not None:
        page_obj = items.filter(name__icontains=item_name)

    paginator = Paginator(page_obj, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, 'bluepage/Firs1t.html', context)

class Ai_tools_ai(ListView):
    model = Ai_tools
    template_name = 'bluepage/Firs1t.html'
    context_object_name = 'items'
    paginate_by = 3
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

class Delete_Ai_tools(DeleteView):
    model = Ai_tools
    template_name = 'bluepage/del_ai.html'
    success_url = reverse_lazy('myapp:baze')
def deleteitem(request, id_my):
    item = Ai_tools.objects.get(id=id_my)
    context = {
        'items': item
    }
    if request.method == "POST":
        item.delete()
        return redirect("/")
    return render(request,'bluepage/del_ai.html', context=context)
