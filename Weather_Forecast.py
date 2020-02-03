import re
import urllib.request
 
condition=1
braces="<"
 
while(condition):
  end=0
  start=0
  city=input("Enter your city to check it's weather fore-cast: ")
  try:
    url="http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"
    rawData = urllib.request.urlopen(url).read()
    data =  rawData.decode("utf-8")
    string = re.search('1 &ndash; 3 Day Weather Forecast Summary:</b><span class="read-more-small"><span class="read-more-content"> <span class="phrase">',data)
    start=string.end()
    i=0
    for i in range(start,start+500):
      if data[i]==braces:
        end=i
        break
 
    weather = data[start:end]
    final = weather.replace("&deg;C"," °C")
    print(final)
    print("")
  except:
    print("No city found! You may have misstyped the city name")
