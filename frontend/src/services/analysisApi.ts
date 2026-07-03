import api from "./api";

export const analyzeSkillGap = async (
  resumeText: string,
  jobText: string
) => {

  const response = await api.post(
    "/analysis/analysis/skill-gap",
    {
      resume_text: resumeText,
      job_text: jobText,
    }
  );

  return response.data;
};