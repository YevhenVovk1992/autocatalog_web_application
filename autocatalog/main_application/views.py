from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

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
            return HttpResponse(str(year) + ' Categories ' + type_id)
        return HttpResponse('Categories ' + type_id)