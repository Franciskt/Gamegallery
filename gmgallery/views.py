
from django.shortcuts import render

from .models import gmgallery


# Create your views here.
def gmgallery_list(request):
    queryset = gmgallery.objects.all()
    context = {
        "gmgallerys": queryset,
            }
    return render(request, 'index.html', context)

# class gmgalleryListView(ListView):
# model = gmgallery
# template_name = 'index.html'
# context_object_name = 'gmgallery'

# def football(request):
# return render(request, 'football.html', {'title': 'football'})
