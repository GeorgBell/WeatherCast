from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
import requests
from weather_n_clothes import forms, addon

# Create your views here.

def index(request, city=None, gender=None):
    """
    Index view:
    - get IP address of user
    - get city by IP address
    - send request to weather API
    - process possible errors
    - form the path to recommended outfit
    - render the index view with weather and clothes data
    """
    # Get city of user unless it is submitted
    if city == None:
        # Get IP address from the request
        #ip = request.META.get('REMOTE_ADDR', None)
        ip = '37.147.237.53' # MOCKUP
        # Get city from IP address
        g = GeoIP2()
        city = g.city(ip)['city']

    # Send request to the Weather API
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=8b382ef4df4488ef794338a7819f3c9d'
        r = requests.get(url.format(city)).json()

        # Parse the weather to dictionary
        city_weather = {
            'flag': True,
            'city': city,
            'temperature': int(r["main"]["temp"]),
            'main': r["weather"][0]["main"],
            'description': r["weather"][0]["description"],
            'icon': r["weather"][0]["icon"],
            }
    except:
        # Fill in the void dictionary
        city_weather = {
            'flag': False,
            'city': "Incorrect city!",
            'temperature': None,
            'main': None,
            'description': None,
            'icon': None,
            }

    # Form the path to the recommended outfit
    cloth_pic = addon.form_cloth_pic_path(gender, city_weather)
    # Form injection dictionary for clothes
    clothes_dict = {'gender': gender, 'cloth_pic': cloth_pic}
    # Form context for insertion to the template
    context = {'city_weather' : city_weather, 'clothes':clothes_dict}
    # Render the index view
    return render(request, 'weather_n_clothes/index.html', context)


def details_selection(request):
    """
    Details view:
    - Create forms to get city and gender data
    - render forms
    - if forms are submitted, render index view with obtained data
    """
    form = forms.FormDetails()

    # Render index view if data submitted
    if request.method == 'POST':
        form = forms.FormDetails(request.POST)
        if form.is_valid():
            return index(request, city=form.cleaned_data['city'], gender=form.cleaned_data['gender'])

    # Render details selection view
    return render(request, 'weather_n_clothes/details_form.html', {'form':form})


def about_view(request):
    """
    About view:
    - render page with project information
    """
    return render(request, 'weather_n_clothes/about.html')
