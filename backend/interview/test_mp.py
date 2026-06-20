import traceback

try:
    import mediapipe as mp

    print("SUCCESS")
    print("Version:", mp.__version__)
    print("Has Solutions:", hasattr(mp, "solutions"))

except Exception:
    traceback.print_exc()