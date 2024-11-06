'''
Flask App Server module
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    function docstring
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Extract the label and score from the response
    if dominant_emotion is None:
        return "Invalid input! Try again."
    return f"For the given statement, the system response is \
                        'anger': {anger}, 'disgust': {disgust}, \
                        'fear': {fear},  'joy': {joy}, and 'sadness': {sadness}. \
                        The dominant emotion is {dominant_emotion}" \

@app.route("/")
def render_index_page():
    '''
    docstring
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
