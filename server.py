'''This module provides back-end functionality'''
from flask import Flask, request, render_template, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__, template_folder='oaqjp-final-project-emb-ai/templates',
             static_folder='oaqjp-final-project-emb-ai/static')

@app.route('/')
def render_page():
    '''This function renders the application's UI'''
    return render_template('index.html')

@app.route('/emotionDetector')
def get_emotion_from_text():
    '''This function provides an endpoint to use for emotion detection'''
    text = request.args.get('textToAnalyze')
    res = emotion_detector(text)
    if res['dominant_emotion'] is not None:
        return jsonify(res)
    return jsonify({"message": "Invalid text! Please try again!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
