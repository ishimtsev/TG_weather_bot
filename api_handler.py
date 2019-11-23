import requests
import json
import config
import keys


def get_currentconditions(location):
    url = "http://dataservice.accuweather.com/currentconditions/v1/"+str(location)
    payload = "apikey="+keys.weather_api_key+"&language=ru&details=true"
    response = requests.get(url, params=payload)
    data = json.loads(response.text)
    s = str(data[0]["Temperature"]["Metric"]["Value"]) + "°C, ощущается как " + str(data[0]["RealFeelTemperature"]["Metric"]["Value"]) + "\n"
    s += str(data[0]["WeatherText"])
    return s


def get_location(query):
    url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete"
    payload = "apikey="+keys.weather_api_key+"&language=ru&q=" + str(query)
    response = requests.get(url, params=payload)

    data = json.loads(response.text)
    if len(data)==0:
        return None
    else:
        results=[]
        for city in data:
            full_str = city["LocalizedName"] + ", " + city["AdministrativeArea"]["LocalizedName"] + ", " + city["Country"]["LocalizedName"]
            temp = config.Result_str(data.index(city)+1, city["LocalizedName"], city["Key"], full_str)
            results.append(temp)
        return results
