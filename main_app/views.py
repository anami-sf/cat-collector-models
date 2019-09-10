from django.shortcuts import render
from .models import Cat
#from django.views.generic import ListView
from django.views.generic.edit import CreateView

# class CatList(ListView):
#     model = Cat

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def cats_index(request):
    cats = Cat.objects.all()
    return render(request, 'cats/index.html', {'cats': cats})


def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)
    return render(request, 'cats/detail.html', {'cat': cat})


# Will display a template with user input form to create a new cat
class CatCreate(CreateView):
    model = Cat
    fields = ['name', 'breed', 'description', 'age']
    # fields = '__all__'  same as ^^^
