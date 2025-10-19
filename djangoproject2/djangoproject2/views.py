# from django.http import HttpResponse
from django.shortcuts import render
def calc(request):
    # return HttpResponse("Hello World!")
    return render(request, 'calc/calc_list.html')
