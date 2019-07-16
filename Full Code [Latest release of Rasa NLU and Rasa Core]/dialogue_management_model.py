from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import rasa_core
from rasa_core.agent import Agent
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.utils import EndpointConfig
from rasa_core.run import serve_application
from rasa_core import config

logger = logging.getLogger(__name__)

def train_dialogue(domain_file = 'weather_domain.yml',
                   model_path = './models/dialogue',
                   training_data_file = './data/stories.md'):

    agent = Agent(domain_file,
                  policies = [
                      MemoizationPolicy(),
                      KerasPolicy(
                          augmentation_factor = 50,
                          max_history=3,
                          epochs=300,
                          batch_size=50,
                          validation_split = 0.2)
                  ])
    data = agent.load_data(training_data_file)

    agent.train(data)

    agent.persist(model_path)
    return agent

def run_weather_bot(serve_forever=True):
    interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
    action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
    agent = Agent.load('./models/dialogue', interpreter=interpreter, action_endpoint=action_endpoint)
    rasa_core.run.serve_application(agent ,channel='cmdline')

    return agent

if __name__ == '__main__':
    train_dialogue()
    run_weather_bot()
