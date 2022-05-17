import requests 
import json 

class yourHoroscope:
  def __init__(self):
    self.api_url = "https://aztro.sameerkumar.website/"
    self.horoscope = ''

  def get(self):
    ''' Method that gets  horoscope
    args: None 
    return: Horoscope '''
    
    response = requests.get(self.api_url)
    horoscope = response.json()
    return horoscope 

  def getHoroscope(self):
    '''
    Gets singular Dog Fact
    args: None
    return: None 
    '''
    self.horoscope = self.get()['horoscope']

 # params = (('sign', 'taurus'),('day', 'today'),)

 # response = requests.get('https://aztro.sameerkumar.website/', params=params)