import requests
answer = 'y'
while answer == 'y':
    zipcode = input('What is your zip code?')
    url = ('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=8d2351c39c1fbec244c8a59227424628&units=imperial')
    r = requests.get(url, auth=('user', 'pass'))
    j = r.json()
    info = (j['main'])
    weathertemp = (info.get('temp'))
    if weathertemp <= 55:
        print('You need a jacket! '+'It is '+ str(weathertemp) +' degrees outside')
    else:
        print('Take that jacket off! '+'It is '+str(weathertemp)+' degrees outside')
    print('Would want to get the weather for another zip code?(y/n)')
    answer = input()
    if answer == 'n':
        print('Thank you for using the weather app')

