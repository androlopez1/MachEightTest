from django.http import HttpResponse
from django.shortcuts import render
import requests
import itertools

from .forms import InputForm

def get_heights(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data.get("user_input")
            url = 'https://mach-eight.uc.r.appspot.com'
            r = requests.get(url)
            res = r.json().get("values")
            response = ([f'- {x["first_name"]} {x["last_name"]} &nbsp {y["first_name"]} {y["last_name"]}<br>'  
                for x,y in itertools.combinations_with_replacement(res,2) if int(x["h_in"])+int(y["h_in"])==user_input])
            if len(response) != 0:
                return HttpResponse(response)
            return HttpResponse("No se encontraron coincidencias")
    else:
        form = InputForm()

    return render(request, 'nbaplayerpairer/input.html', {'form': form})