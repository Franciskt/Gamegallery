from django.shortcuts import render
from django.views.generic import ListView

from .models import gmgallery


# Create your views here.
def Gmgallery_list(request):
    queryset = gmgallery.objects.all()
    context = {
                 "gmgallery": queryset,
            }
    return render(request, "index.html", context)


class gmgalleryView(ListView):
    model = gmgallery


def football(request):
    return render(request, 'football.html', {'title': 'football'})
