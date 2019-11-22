from django.shortcuts import render

# Create your views here.


def site_index(request):
    return render(request, 'index.html')

