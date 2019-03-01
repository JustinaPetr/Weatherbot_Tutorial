# Weatherbot Tutorial (using the latest release of Rasa NLU and Rasa Core)

Rasa NLU and Rasa Core devs are doing an amazing job improving both of these libraries which results in code changes for one method or another. In fact, since I recorded a Wetherbot tutorial,
there were quite a few changes which were introduced to Rasa NLU and Rasa Core. On 30th of August, Rasa v.0.11 was released with a lot of changes under the hood. This repo contains the updated weatherbot code compatible with the latest releases of Rasa Core and Rasa NLU.

## How to use this repo

The code of this repo differs quite significantly from the original video. This is how to use it:

### Training the NLU model

Training of the NLU model didn't change much from the way it was shown in the video. To train and test the model run:  

``` python nlu_model.py ```

### Training the Rasa Core model

The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Open a new terminal and train the Rasa Core model by running:  

``` python dialogue_management_model.py```  
 
3. Talk to the chatbot once it's loaded.  

### Starting the interactive training session:

The process of running the interactive session is very similar to training the Rasa Core model:
1. Make sure the custom actions server is running:  

``` python -m rasa_core_sdk.endpoint --actions actions ```  

2. Start the interactive training session by running:  

``` python train_interactive.py ```  

### Connecting a chatbot to Slack:
1. Configure the slack app as shown in the video  
2. Make sure custom actions server is running  
3. Start the agent by running run_app.py file (don't forget to provide the slack_token)  
4. Start the ngrok on the port 5004  
5. Provide the url: https://your_ngrok_url/webhooks/slack/webhook to 'Event Subscriptions' page of the slack configuration.  
6. Talk to you bot.  

I will do my best to keep this repo up-to-date, but if you encounter any issues with using the code, please raise an issue or drop me a message :)

Latest code update: 01/03/2019

Latest compatible Rasa NLU version: 0.14.4
Latest compatible Rasa Core version: 0.13.2





