from django.shortcuts import render

from .forms import ItemForms

# Create your views here.


def index(request):
    form = ItemForms()
    if request.method == 'POST':
        print(request.POST)

    #form = ItemForms()
    context = {'form': form}
    return render(request, 'app/index.html', context)


def create(request, pk):
    return render(request, id=pk)
