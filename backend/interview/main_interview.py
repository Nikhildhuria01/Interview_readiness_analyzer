import threading

from mock_interview import run_camera_interview

from mock_interview_engine import run_audio_interview


camera_thread = threading.Thread(
    target=run_camera_interview
)

camera_thread.start()

run_audio_interview()

camera_thread.join()

print(
    "\nFull Interview Completed!"
)