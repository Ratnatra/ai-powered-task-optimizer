import random

# Sample tasks for each emotion
task_recommendations = {
    'Happy': ['Collaborate on a creative project', 'Plan a team-building activity'],
    'Sad': ['Take a short break', 'Engage in a relaxing task'],
    'Angry': ['Practice deep breathing exercises', 'Work on a low-stress task'],
    'Surprise': ['Share the exciting news with the team', 'Work on innovative ideas'],
    'Neutral': ['Continue with regular tasks', 'Organize the workspace'],
    'Fear': ['Seek support from a colleague', 'Work on a familiar task'],
    'Disgust': ['Take a walk to clear the mind', 'Work on a different task']
}

def recommend_task(emotion):
    """
    Recommend a task based on the detected emotion.
    :param emotion: Detected emotion.
    :return: Recommended task.
    """
    return random.choice(task_recommendations.get(emotion, ['Focus on regular tasks']))