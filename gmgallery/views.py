from django.shortcuts import render
from .models import gmgallery

# Create your views here.
def Gmgallery_list(request):
    queryset = gmgallery.objects.all()
    context = {
                 "gmgallery": queryset,
            }
    return render(request, "index.html", context)