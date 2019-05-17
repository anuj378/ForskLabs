import requests
print("Enter the city you want to have the status of: \n")
city=input()
url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q="+city
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)

response = requests.get(url)
#response.text
data=response.json()
data
print("LATITUDE AND LOGITUDE ARE : " , data['coord']['lat'] ," and " ,data['coord']['lon'])
print('WEATHER CONDITIONS : ',data["weather"][0]["main"])
print('WIND SPEED' ,data["wind"]["speed"])
print('Sunset' , data["sys"]["sunset"])
print('Sunrise' , data["sys"]["sunrise"])