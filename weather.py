#! /usr/bin/python3
import requests
import subprocess

from bs4 import BeautifulSoup

def weatherRequest() :
    # GET REQUEST
    res = requests.get('https://weather.com/fr-FR/temps/aujour/l/9a50f3f9c14d9540347228e1db60f16fa60f55001adc893b17abfc3b44a7adac')

    # SOUP OBJECT
    soup = BeautifulSoup(res.content, 'html.parser')

    # DATA
    city = soup.find('h1').text
    hour = soup.find('div', 'CurrentConditions--timestamp--1SWy5').text
    degree = soup.find('span', 'CurrentConditions--tempValue--3KcTQ').text
    description = soup.find('div', 'CurrentConditions--phraseValue--2xXSr').text
    airQuality = soup.find('text','DonutChart--innerValue--k2Z7I').text
    airQualityLabel = soup.find('span','AirQualityText--severity--1VMr2').text

    # SEND NOTIF
    return subprocess.Popen(['notify-send', city + '\n' + hour + '\n' + degree + ' ' + description+ '\n' + airQualityLabel + ' ' + airQuality])

weatherRequest()