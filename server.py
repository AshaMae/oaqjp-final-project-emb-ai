from flask import Flask, render_template, resuest
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector") 
def emot_detector():
    text_to_analyse = request.args.get('textToAnalyse')
    dominant_emotion = emotion_detector(text_to_analyse)
    if dominant_emotion if None:
        return "Invalid text! PLease Try Again"
    else:
        return "For the given statement, the system response is {}.".format()