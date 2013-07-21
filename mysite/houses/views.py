from django.shortcuts import render

from houses.models import House, Owner

def index(request):
    house_list = House.objects.all().order_by('owner')
    context = {'house_list': house_list}
    return render(request, 'houses/index.html', context)