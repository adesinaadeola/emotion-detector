import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = obj, headers=header)
    formatted_response = json.loads(response.text)['emotionPredictions']
    for key in formatted_response:
        dict_output = key['emotion']
    max_value = max(dict_output.values())
    dict_output['dominant_emotion'] = max_value

    return dict_output