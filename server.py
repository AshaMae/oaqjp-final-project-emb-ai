from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/emotionDetector") 
def emotionDetector():
    text_to_analyse = request.args.get('textToAnalyse')
    dominant_emotion = emotion_detector(text_to_analyse)
    if dominant_emotion is None:
        return "Invalid text! PLease Try Again"
    else:
        return "For the given statement, the system response is {}.".format(dominant_emotion)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)