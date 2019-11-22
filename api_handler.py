import requests
import json
import config
import keys


def get_currentconditions(location):
    url = "http://dataservice.accuweather.com/currentconditions/v1/"+str(location) #291102
    payload = "apikey="+keys.weather_api_key+"&language=ru&details=true"
    response = requests.get(url, params=payload)

    print(response.url) #
    print(response.text) #
    data = json.loads(response.text)
    s = "*"+"*\n\n"
    s += str(data[0]["Temperature"]["Metric"]["Value"]) + "°C, ощущается как " + str(data[0]["RealFeelTemperature"]["Metric"]["Value"]) + "\n"
    s += str(data[0]["WeatherText"])
    print(s)
    # print(a[0])
    # print(a[0]["Temperature"]["Metric"]["Value"])
    return s


def get_location(query):
    url = "http://dataservice.accuweather.com/locations/v1/cities/autocomplete"
    payload = "apikey="+keys.weather_api_key+"&language=ru&q=" + str(query) #тюмень
    response = requests.get(url, params=payload)

    print(response.url)  #
    print(response.text)  #

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


            # mas.append([data.index(city)+1, city["LocalizedName"], city["Key"]])
            #
            # cities_list[data.index(city)+1]=city["Key"]
            # s+="*"+str(data.index(city)+1)+"*. "+city_str+"\n"
        #s+="\nНапишите номер города, чтобы узнать погоду."
        #return s

    # print(len(data))
    # print(data)
    # data = json.loads(response.text)
    # s = "<b>Погода в Тюмени</b>\n\n"
    # s += str(data[0]["Temperature"]["Metric"]["Value"]) + "°C, ощущается как " + str(
    #     data[0]["RealFeelTemperature"]["Metric"]["Value"]) + "\n"
    # s += str(data[0]["WeatherText"])
    # print(s)













#get_currentconditions(291102)
# get_location("тюмень")
print(get_location("тываом"))