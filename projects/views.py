from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def project_list(request):
#     # an httpreponse object returns html
#     return HttpResponse("<h1>Hello world!</h1>")


def project_list(request):
    # an httpreponse object returns html
    return render(request, 'projects/index.html')