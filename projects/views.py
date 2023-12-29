from django.shortcuts import render
# from django.http import HttpResponse
from projects.models import Project

# Create your views here.
# def project_list(request):
#     # an httpreponse object returns html
#     return HttpResponse("<h1>Hello world!</h1>")

def all_projects(request):
    # query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})