from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView
from .forms import *


'''
 #Этап 1
class ListCarsView(ListView):

      model = Cars
      template_name = 'cars.html'
      context_object_name = 'cars'
'''


def car_view(request):
    if request.method == 'POST':
        form = SelectForm(request.POST)
        if form.is_valid():
            model = request.POST.get('models_cars')
            if model is None or model == '':
                car = Cars.objects.all()
                return render(request, 'cars.html', locals())
            car = Cars.objects.filter(name=model)
            return render(request, 'cars.html', locals())
    form = SelectForm()
    return render(request, 'cars.html', locals())