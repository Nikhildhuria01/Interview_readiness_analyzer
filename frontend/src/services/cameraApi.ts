import api from "./api";

export const analyzeCameraFrame = async (
    frame: string
) => {

    const response = await api.post(
        "/camera/analyze-frame",
        {
            frame,
        }
    );

    return response.data;
};