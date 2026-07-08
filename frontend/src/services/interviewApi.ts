import api from "./api";

/*
 * Old API
 * Kept for debugging and individual testing.
 */
export const analyzeInterview = async (
    question: string,
    audioFile: Blob
) => {

    const formData = new FormData();

    formData.append("question", question);
    formData.append("audio", audioFile, "answer.webm");

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

export const endInterview = async () => {
    return api.post("/interview/end");
};
/*
 * New API
 * Sends the complete interview to the backend.
 */
/*
export const analyzeCompleteInterview = async (
    questions: string[],
    recordings: Blob[]
) => {

    const formData = new FormData();

    questions.forEach((question) => {
        formData.append("questions", question);
    });

    recordings.forEach((recording, index) => {
        formData.append(
            "recordings",
            recording,
            `question_${index + 1}.webm`
        );
    });

    const response = await api.post(
        "/interview/analyze-complete",
        formData,
        {
            headers: {
                "Content-Type": "multipart/form-data",
            },
        }
    );

    return response.data;
};
*/