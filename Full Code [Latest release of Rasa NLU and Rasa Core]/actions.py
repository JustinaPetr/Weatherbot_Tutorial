from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import os


class ActionWeather(Action):
    def name(self):
        return 'action_weather'
        
    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient

        # You need to provide APIXUKEY in file export_APIXU_KEY.sh since it won't be saved in GIT
        #
        # http://api.apixu.com/v1/current.json?key=<apixu_key...>&q=paris
        try:
            #print(os.environ)
            print("APIXU_KEY=" + os.environ["APIXU_KEY"])
            api_key = os.environ['APIXU_KEY']
            # api_key = 'xxxx' #your apixu key
            client = ApixuClient(api_key)
        except KeyError:
            print("Please set the environment variable APIXU_KEY")
            os.sys.exit(1)
        
        loc = tracker.get_slot('location')
        current = client.current(q=loc)
        
        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        humidity = current['current']['humidity']
        wind_mph = current['current']['wind_mph']

        response = """It is currently {} in {} at the moment. 
        The temperature is {} degrees, the humidity is {}% and the wind speed is {} mph."""\
            .format(condition, city, temperature_c, humidity, wind_mph)
                        
        dispatcher.utter_message(response)
        return [SlotSet('location',loc)]

