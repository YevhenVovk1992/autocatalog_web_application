import datetime
import time

from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views import View


# Create your views here.

def page_not_found(request, exception):
    return HttpResponse("<h1>Page not found</h1>")


class MainPageView(View):

    def get(self, request):
        """
        Start page of the web site
        """

        return HttpResponse('Main_page')


class CategoriesView(View):

    def get(self, request, type_id, year=None):
        """
        Get categories of cars
        """
        if year:
            if year > int(datetime.date.today().year):
                raise Http404()
            return HttpResponse(str(year) + ' Categories ' + type_id)
        return HttpResponse('Categories ' + type_id)


