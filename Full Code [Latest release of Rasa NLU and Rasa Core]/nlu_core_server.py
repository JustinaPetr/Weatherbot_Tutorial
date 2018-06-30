from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

from rasa_core.channels import HttpInputChannel
from rasa_core import utils
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.channels.channel import UserMessage
from rasa_core.channels.direct import CollectingOutputChannel
from rasa_core.channels.rest import HttpInputComponent
from flask import Blueprint, request, jsonify

logger = logging.getLogger(__name__)
class SimpleWebBot(HttpInputComponent):
    """A simple web bot that listens on a url and responds."""

    def blueprint(self, on_new_message):
        custom_webhook = Blueprint('custom_webhook', __name__)

        @custom_webhook.route("/status", methods=['GET'])
        def health():
            return jsonify({"status": "ok"})

        @custom_webhook.route("/", methods=['POST'])
        def receive():
            payload = request.json
            sender_id = payload.get("sender", None)
            text = payload.get("message", None)
            print("message received ",text)

            out = CollectingOutputChannel()
            on_new_message(UserMessage(text, out, sender_id))
            # responses = [m for _, m in out.messages]
            print("output looks like")
            print(out)
            print("output msg looks like")
            print(out.messages)

            responses=None
            if len(out.messages)>=1:
                responses=out.messages[0]["text"]

            # responses = [m["text"] for _, m in out.messages]
            print("responses")
            print(responses)
            return jsonify(responses)
    
        return custom_webhook

def run_nlu_core_server(port_number,serve_forever=True):

    #path to your NLU model
    # interpreter = RasaNLUInterpreter("./models/nlu/default/weathernlu")
    interpreter = "./models/nlu/default/weathernlu"
    # path to your dialogues models
    agent = Agent.load("./models/dialogue", interpreter=interpreter)
    #http api endpoint for responses
    input_channel = SimpleWebBot()
    if serve_forever:
        agent.handle_channel(HttpInputChannel(port_number, "/chat", input_channel))
    return agent




if __name__ == '__main__':
    port_number=5003
    print("Runnng rasa_core server at port #"+str(port_number))
    print("Sample request")
    print("url:http://localhost:"+str(port_number)+"/chat/")
    print("url_type:POST")
    print("request body type:raw(application/json)")
    print('sample request:{ "sender": "default", "message": "how is the weather in Dublin"}')
    run_nlu_core_server(port_number)
    print("run_nlu_core_server runnng")
