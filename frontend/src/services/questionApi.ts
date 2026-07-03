import api from "./api";

export const generateQuestions = async (
  resumeText: string,
  jobText: string
) => {

  const response = await api.post(
    "/questions/questions/generate",
    {
      resume_text: resumeText,
      job_text: jobText,
    }
  );

  return response.data;

};