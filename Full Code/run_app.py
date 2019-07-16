from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

import os

# You need to provide APIXUKEY in file export_APIXU_KEY.sh since it won't be saved in GIT
#
# http://api.apixu.com/v1/current.json?key=<apixu_key>&q=paris
try:
    #print(os.environ)
    print("Bot_User_OAuth_Access_Token=" + os.environ["Bot_User_OAuth_Access_Token"])
    Bot_User_OAuth_Access_Token = os.environ['Bot_User_OAuth_Access_Token']
except KeyError:
    print("Please set the environment variable 'Bot_User_OAuth_Access_Token'")
    sys.exit(1)

#input_channel = SlackInput('xoxb...' #your bot user authentication token)
input_channel = SlackInput(Bot_User_OAuth_Access_Token)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

agent = Agent.load('./models/dialogue', 
             interpreter = nlu_interpreter, 
             action_endpoint = action_endpoint)


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

#input_channel = SlackInput('xoxp...', #app verification token
#							'xoxb...', # bot verification token
#							'...', # slack verification token
#							True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
