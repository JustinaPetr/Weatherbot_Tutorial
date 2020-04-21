# Weatherbot Tutorial (using the latest release of Rasa)

**Disclaimer: This project is not an official Rasa tutorial. 
While it's a good source to learn about Rasa, I would recommend
also checking out official Rasa education sources like 
[Rasa Masterclass](https://www.youtube.com/playlist?list=PL75e0qA87dlHQny7z43NduZHPo6qd-cRc).**


Rasa devs are doing an amazing job improving this library which results in code changes for one method or another. In fact, since I recorded a Wetherbot tutorial,
there were quite a few changes which were introduced to Rasa (former Rasa NLU and Rasa Core). This repo contains the updated weatherbot code compatible with the latest release of Rasa.

## How to use this repo

The code of this repo differs quite significantly from the original video. This is how to use it:

### Training the NLU model

Since the release of Rasa 1.0, the training of the NLU models became a lot easier with the new CLI. Train the model by running:  

```rasa train nlu ```

Once the model is trained, test the model:

```rasa shell nlu```


### Training the dialogue model

The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:  
1. Start the custom action server by running:  

``` rasa run actions```  

2. Open a new terminal and train the Rasa Core model by running:  

``` rasa train```  
 
3. Talk to the chatbot once it's loaded after running:  
```rasa shell```  


### Starting the interactive training session:

To run your assistant in a interactive learning session, run:
1. Make sure the custom actions server is running:  

```rasa run actions```  

2. Start the interactive training session by running:  

```rasa interactive```  

### Connecting a chatbot to Slack:
1. Configure the slack app as shown in the video  
2. Provide the slack configuration tokens in a credentials.yml file  
3. Make sure custom actions server is running  
4. Start the agent by running `rasa run`
5. Start the ngrok on the port 5004  
6. Provide the url: https://your_ngrok_url/webhooks/slack/webhook to 'Event Subscriptions' page of the slack configuration.  
7. Talk to you bot.  

I will do my best to keep this repo up-to-date, but if you encounter any issues with using the code, please raise an issue or drop me a message :)

Latest code update: 31/04/2020

Latest compatible Rasa version: 1.9.6





