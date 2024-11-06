import requests
import json

def emotion_detector(text_to_analyze):
   # Define the URL for the sentiment analysis API
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
  
    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        emotion_dictionary = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_dictionary['anger']
        disgust = emotion_dictionary['disgust']
        fear = emotion_dictionary['fear']
        joy = emotion_dictionary['joy']
        sadness = emotion_dictionary['sadness']
        dominant_emotion = max(emotion_dictionary, key=emotion_dictionary.get)

    # If the response status code is 500, set label and score to None
    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    # Return the label and score in a dictionary
    return {'anger': anger, 'disgust': disgust,
            'fear' : fear, 'joy': joy,
            'sadness': sadness, 
            'dominant_emotion': dominant_emotion}