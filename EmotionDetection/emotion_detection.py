import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    reqHeaders = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    reqJson = { "raw_document": { "text": text_to_analyse } }

    res = requests.post(url, headers = reqHeaders, json = reqJson)
    
    if (res.status_code == 200):
        maxEmotionVal = 0.00
        maxEmotion = ''
        emotionPredictions = json.loads(res.text)['emotionPredictions'][0]['emotion']

        output = {}
        for emotion in emotionPredictions:
            output[emotion] = emotionPredictions[emotion]
            if (emotionPredictions[emotion] > maxEmotionVal):
                maxEmotion = emotion
                maxEmotionVal = emotionPredictions[emotion]
        
        output['dominant_emotion'] = maxEmotion
    else:
        output = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    return output

