from flask import render_template, request, jsonify
from app import app
from app.models.emotion_detection import detect_emotion_from_image, detect_emotion_from_text, detect_emotion_from_audio
from app.models.task_recommendation import recommend_task

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    text_input = request.form.get('text_input')
    video_input = request.files.get('video_input')
    audio_input = request.files.get('audio_input')

    if text_input:
        emotion = detect_emotion_from_text(text_input)
    elif video_input:
        video_input.save('uploaded_video.mp4')
        emotion = detect_emotion_from_image('uploaded_video.mp4')  # Placeholder for video processing
    elif audio_input:
        audio_input.save('uploaded_audio.wav')
        emotion = detect_emotion_from_audio('uploaded_audio.wav')
    else:
        return jsonify({'error': 'No input provided'}), 400

    return jsonify({'emotion': emotion})

@app.route('/recommend_task', methods=['POST'])
def recommend_task_route():
    mood = request.form.get('mood')
    if not mood:
        return jsonify({'error': 'No mood provided'}), 400

    task = recommend_task(mood)
    return jsonify({'task': task})