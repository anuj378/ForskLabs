import requests
#api key : ed7e5c7f17b81f5ab78f
url1 ='https://free.currconv.com'
url2='/api/v7/convert?q=USD_INR,INR_USD&compact=ultra&apiKey=ed7e5c7f17b81f5ab78f'
url=url1+url2
response = requests.get(url)
#response.text
data=response.json()
data
