from pydantic import BaseModel


class CameraFrame(BaseModel):
    frame: str