from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter

from rasa_core.utils import EndpointConfig

import os

try:
    #print(os.environ)
    print("Bot_User_OAuth_Access_Token=" + os.environ["Bot_User_OAuth_Access_Token"])
    Bot_User_OAuth_Access_Token = os.environ['Bot_User_OAuth_Access_Token']
except KeyError:
    print("Please set the environment variable 'Bot_User_OAuth_Access_Token'")
    os.sys.exit(1)

#input_channel = SlackInput('xoxb...' #your bot user authentication token)
input_channel = SlackInput(Bot_User_OAuth_Access_Token)

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")

agent = Agent.load('./models/dialogue', 
             interpreter = nlu_interpreter, 
             action_endpoint = action_endpoint)

# You need to setup Slack API's "Event Subscriptions" after you "grok http 5004" after this script running up:
# 1.) 
# http://XXXXXXX.ngrok.io/webhooks/slack/webhook (watch out the routes and the grok's URL)

agent.handle_channels([input_channel], 5004, serve_forever=True)
