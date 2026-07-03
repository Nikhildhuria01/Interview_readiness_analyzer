import api from "./api";

export const analyzeInterview = async (
    question: string,
    audioFile: Blob
) => {

    const formData = new FormData();

    formData.append("question", question);

    formData.append("audio", audioFile, "answer.wav");

    const response = await api.post(
        "/interview/analyze",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};