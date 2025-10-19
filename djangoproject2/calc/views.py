from django.shortcuts import render

# Create your views here.
def calc_list(request):
    return render(request, 'calc/calc_list.html')
