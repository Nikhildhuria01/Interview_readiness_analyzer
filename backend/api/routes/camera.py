import base64
import cv2
import numpy as np
import threading
from fastapi import APIRouter
from backend.api.schemas.camera import CameraFrame
from backend.interview.eye_contact_analysis import get_eye_contact_score
from backend.interview.posture_analysis import get_posture_score
from backend.interview.head_stability import get_head_stability_score
router = APIRouter()
camera_lock = threading.Lock()

@router.post("/analyze-frame")
def analyze_frame(data: CameraFrame):

    try:

        # Remove the Base64 prefix
        image_data = data.frame.split(",")[1]

        # Decode Base64 string
        image_bytes = base64.b64decode(image_data)

        # Convert bytes → numpy array
        image_array = np.frombuffer(image_bytes, dtype=np.uint8)

        # Convert numpy array → OpenCV image
        frame = cv2.imdecode(
            image_array,
            cv2.IMREAD_COLOR
        )

        if frame is None:

            return {
                "success": False,
                "message": "Failed to decode image."
            }

        with camera_lock:
            eye_score = get_eye_contact_score(frame)

            posture_score = get_posture_score(frame)

            head_score = get_head_stability_score(frame)

        return {

            "success": True,

            "eye_contact": eye_score,

            "posture": posture_score,

            "head_stability": head_score

    }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)

        }