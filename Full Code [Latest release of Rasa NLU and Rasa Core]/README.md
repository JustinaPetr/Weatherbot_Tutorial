
# Weatherbot Tutorial (using the latest release of Rasa NLU and Rasa Core)  
  
Rasa NLU and Rasa Core devs are doing an amazing job improving both of these libraries 
which results in code changes for one method or another. In fact, since I recorded 
a Wetherbot tutorial, there were quite a few changes which were introduced to Rasa NLU and Rasa Core. On 30th of August, Rasa v.0.11 was released with a lot of changes under the hood. This repo contains the updated weatherbot code compatible with the latest releases of Rasa Core and Rasa NLU.  
  
## How to use this repo  
  
The code of this repo differs quite significantly from the original video. 
The following explains the overall steps/flows:

* Step-1: Training the NLU model
* Step-2: (Initial) Training the Rasa Core model
* Step-3: Optional -- (Interactive / Online) Training Session for the Rasa Core model
* Step-4: Deploy Rasa Chat Bot (NLU + Core/Agent + Action) to work with Slack Chat.
  
### Step-1: Training the NLU model  
  
Training of the NLU model didn't change much from the way it was shown in the video. To train and test the model run:    

```
python nlu_model.py
```
  
### Step-2: (Initial) Training the Rasa Core model  
  
The biggest change in how Rasa Core model works is that custom action 'action_weather' now needs to run on a separate server. That server has to be configured in a 'endpoints.yml' file.  This is how to train and run the dialogue management model:

1. Start the custom action server by running:
  
    ``` 
    APIXU_KEY=<APIXU_token> python -m rasa_core_sdk.endpoint --actions actions
    ``` 
    or, if you already export Key and Token in each terminal above:

    ```
    python -m rasa_core_sdk.endpoint --actions actions
    ```

2. Open a new terminal and train the Rasa Core model by running:
      
    ``` 
    python dialogue_management_model.py
    ```

3. Talk to the chatbot once it's loaded to provide training with `intended / corrected behaviors` for the Rasa Core to learn from your correct answers that you provide. (To exit the interative/online training session, CTRL-C twice!)
  
### Step-3: Optional -- (Interactive / Online) Training Session for the Rasa Core model 
  
The process of running the interactive session is very similar to training the Rasa Core model:

1. Make sure the custom actions server is running:

    ```
    python -m rasa_core_sdk.endpoint --actions actions
    ```

2. Start the interactive training session by running:
  
    ```
    python train_interactive.py 
    ```

### Step-4: Deploy Rasa Chat Bot (NLU + Core/Agent + Action) to work with Slack Chat. 

1. Configure the slack app as shown in the video

	* Study the Video: [From zero to hero: Creating a chatbot with Rasa NLU and Rasa Core](https://player.vimeo.com/video/254777331)
    * See also the screenshots in ./doc folder
    * Go to [apixu web site](https://www.apixu.com/) to 
        create API key `APIXU_KEY=<nnnn...>` .
    * Go to [SlackAPI](https://api.slack.com/) to 
        create "weatherbot" to get `Bot_User_OAuth_Access_Token=<xoxb-...>` for `run_app.py` to consume
    * Go to [ngrok - secure introspectable tunnels to localhost](https://ngrok.com/) to 
        down and install ngrok.
    * Open 3 extra Terminals for `Action, run_app.py, ngrok`
    * Export `Key (obatined from Weather APIXU Key)` and 
    `Token (obtained from Slack Bot User)` in each terminal of those three terminals
    
    Test Weather API (APIXU) with your `APIXU token` before you proceed:

    ```
    Current Weather
    HTTP: http://api.apixu.com/v1/current.json?key=<apixu_key>&q=Paris
    HTTPS: https://api.apixu.com/v1/current.json?key=<apixu_key>&q=Paris
    
    Forecast Weather
    HTTP: http://api.apixu.com/v1/forecast.json?key=<apixu_key>&q=Paris
    HTTPS: https://api.apixu.com/v1/forecast.json?key=<apixu_key>&q=Paris
    ```

2. Run Dialogue (rasa-core) test  

```  
(Try the following and kill it when done testing)  
APIXU_KEY=<nnnn...> python dialogue_management_model.py 
``` 

or, if you already export Key and Token in each terminal above:

```
python dialogue_management_model.py 
```

And, you will enter test conversation such as

```
Processed Story Blocks: 100%|██████████████████████████████████████| 10/10 [00:00<00:00, 1201.39it/s, # trackers=3]
Processed Story Blocks: 100%|██████████████████████████████████████| 10/10 [00:00<00:00, 566.00it/s, # trackers=6]
Processed Story Blocks: 100%|██████████████████████████████████████| 10/10 [00:00<00:00, 515.51it/s, # trackers=6]
Processed actions: 39it [00:00, 11900.90it/s, # examples=39]
2019-05-17 10:58:37.061541: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: FMA
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
masking (Masking)            (None, 3, 16)             0         
_________________________________________________________________
lstm (LSTM)                  (None, 32)                6272      
_________________________________________________________________
dense (Dense)                (None, 11)                363       
_________________________________________________________________
activation (Activation)      (None, 11)                0         
=================================================================
Total params: 6,635
Trainable params: 6,635
Non-trainable params: 0
_________________________________________________________________

... (ignored screen dump before)

Epoch 298/300
25/25 [==============================] - 0s 213us/step - loss: 0.3034 - acc: 0.9600
Epoch 299/300
25/25 [==============================] - 0s 319us/step - loss: 0.2905 - acc: 1.0000
Epoch 300/300
25/25 [==============================] - 0s 235us/step - loss: 0.2877 - acc: 0.9200
Bot loaded. Type a message and press enter (use '/stop' to exit): 
Your input ->  hello                                                                                               
Hello! How can I help?
127.0.0.1 - - [2019-05-17 10:58:52] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 222 0.248822
Your input ->  tell me the weather                                                                                 
In what location?
127.0.0.1 - - [2019-05-17 10:58:58] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 217 0.044651
Your input ->  in London                                                                                           
It is currently Overcast in London at the moment. The temperature is 13.0 degrees, the humidity is 77% and the wind speed is 9.4 mph.
127.0.0.1 - - [2019-05-17 10:59:02] "POST /webhooks/rest/webhook?stream=true&token= HTTP/1.1" 200 333 0.329568
Your input ->        

(CTRL+C twice to quit)                                                                                    
```
  
3. Make sure custom actions server is running  

    ```  
    APIXU_KEY=<nnnn...> python -m rasa_core_sdk.endpoint --actions actions
    ``` 

    or, if you already export Key and Token in each terminal:

    ```
    python -m rasa_core_sdk.endpoint --actions actions
    ```  
  
4. Start the agent by running run_app.py file (don't forget to provide the slack_token)    

    ```  
    Bot_User_OAuth_Access_Token=<xoxb-...> python run_app.py  
    ``` 

    or, if you already export Key and Token in each terminal:

    ```
    python run_app.py
    ```  
   
5. Start the ngrok on the port 5004    

    ```  
    ngrok http 5004
    ```
      
    And, you will see like below:

    ```
    ngrok by @inconshreveable                                                                          (Ctrl+C to quit)  
      Session Status                online Account                       Jim Kowalski (Plan: Free) Update                        update available (version 2.3.28, Ctrl-U to update) Version                       2.3.27 Region                        United States (us) Web Interface                 http://127.0.0.1:4040 Forwarding                    http://92239ac7.ngrok.io -> http://localhost:5004 Forwarding                    https://92239ac7.ngrok.io -> http://localhost:5004                                     
     Connections                   ttl     opn     rt1     rt5     p50     p90                                            
    0       0       0.00    0.00    0.00    0.00 
    ```  

    Then, open ngrok monitor URL using Web browser, Firefox or Chrome or any:

    ``` 
    http://127.0.0.1:4040  
    ```  

6. Provide the ngrok url to 'Event Subscriptions' page of the slack configuration.     

    ```
    https://<your_ngrok_url>/webhooks/slack/webhook` 
    ```

    And, test the connection for ngrok:

    ```
    http://localhost:5004/webhooks/slack/webhook
    http://<ngrok_URL>/webhooks/slack/webhook
    ```

    Now, it's ready for end-to-end test of the Rasa Chat Bot + Slack Chat integration with Weather API called by Rasa SDK Action.
    
7. Talk to your Slack bot using Slack Chat, e.g.

    ```
    https://<your-Slack-Channel>.slack.com/messages/ 
    e.g. 
    https://openkbsorg.slack.com/messages/  
    ```    

I will do my best to keep this repo up-to-date, but if you encounter any issues with using the code, please raise an issue or drop me a message :)

Latest code update: 05/17/2019

Latest compatible Rasa NLU version: 0.14.6
Latest compatible Rasa Core version: 0.13.7
