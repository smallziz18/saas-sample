from django.http import HttpResponse
import pathlib
from django.shortcuts import render
from visits.models import PageViste


def Accueil(request,*argrs,**kwargs):
    queryset = PageViste.objects.filter(path=request.path)
    total_count = PageViste.objects.all()
    
    my_title = " My page"
    my_context = {
        "page_title": my_title,
        "page_visits_count" : queryset.count(),
        "total_visit" : total_count.count,
        "percent" : (queryset.count()*100.0)/total_count.count()
                }
    html_template = "home.html"
    PageViste.objects.create(path = request.path)
    return render(request,html_template,my_context)