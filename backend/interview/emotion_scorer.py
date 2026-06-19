def calculate_emotion_scores(emotion):

    confidence = 50
    engagement = 50
    nervousness = 50

    emotion = emotion.lower()

    if emotion == "happy":

        confidence = 90
        engagement = 85
        nervousness = 10

    elif emotion == "neutral":

        confidence = 75
        engagement = 70
        nervousness = 20

    elif emotion == "surprise":

        confidence = 60
        engagement = 80
        nervousness = 35

    elif emotion == "sad":

        confidence = 35
        engagement = 40
        nervousness = 75

    elif emotion == "fear":

        confidence = 25
        engagement = 45
        nervousness = 90

    elif emotion == "angry":

        confidence = 50
        engagement = 65
        nervousness = 70

    return {

        "confidence_score": confidence,

        "engagement_score": engagement,

        "nervousness_score": nervousness
    }