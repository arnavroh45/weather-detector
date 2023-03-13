import json
import urllib.request
from django.shortcuts import render


# Create your views here.
def index(request):
    if request.method == 'POST' :
        city = request.POST['City']
        res = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=8d3dca177a5d41ed50e8eb9c00e5e10d').read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + 
            str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp'])+'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city=''
        data = {}
    return render(request, 'index.html', {'city':city, 'data':data})  
