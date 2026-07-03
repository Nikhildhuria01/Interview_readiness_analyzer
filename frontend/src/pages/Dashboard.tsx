import { useState } from "react";

import UploadCard from "../components/UploadCard";
import JobDescriptionCard from "../components/JobDescriptionCard";

import { uploadResume } from "../services/resumeApi";
import { analyzeSkillGap } from "../services/analysisApi";
import { generateQuestions } from "../services/questionApi";
import { useNavigate } from "react-router-dom";

export default function Dashboard() {

  const [skills, setSkills] = useState<string[]>([]);

  const [resumeText, setResumeText] = useState("");

  const [jobText, setJobText] = useState("");

  const [matched, setMatched] = useState<string[]>([]);

  const [missing, setMissing] = useState<string[]>([]);

  const [readiness, setReadiness] = useState(0);
  const [questions, setQuestions] = useState<string[]>([]);
  const navigate = useNavigate();

  const handleResume = async (file: File) => {

    try {

      const result = await uploadResume(file);

      setSkills(result.skills);

      setResumeText(result.resume_text);

    } catch (err) {

      console.error(err);

      alert("Resume upload failed.");

    }

  };

  const analyze = async () => {

    if (!resumeText) {

      alert("Please upload your resume first.");

      return;

    }

    if (!jobText.trim()) {

      alert("Please paste the Job Description.");

      return;

    }

    try {

      const result = await analyzeSkillGap(
        resumeText,
        jobText
      );

      setMatched(result.matched_skills);

setMissing(result.missing_skills);

setReadiness(result.readiness_percentage);

      // We will display these later
      setMatched(result.matched_skills || []);

      setMissing(result.missing_skills || []);

      setReadiness(result.readiness_percentage || 0);

    } catch (err) {

      console.error(err);

      alert("Analysis failed.");

    }

  };
  const generateInterviewQuestions = async () => {

    if (!resumeText || !jobText) {

        alert("Please complete the analysis first.");

        return;

    }

    try {

        const result = await generateQuestions(
            resumeText,
            jobText
        );

        console.log(result);

        setQuestions(result.questions);

    }

    catch (err) {

        console.error(err);

        alert("Failed to generate questions.");

    }

};

  return (

    <div className="min-h-screen bg-slate-950 px-10 py-20">

      <h1 className="text-5xl text-white font-bold text-center mb-16">
        AI Dashboard
      </h1>

      <div className="grid md:grid-cols-2 gap-10 max-w-6xl mx-auto">

        <UploadCard
          title="Upload Resume"
          description="Upload your Resume PDF"
          buttonText="Choose Resume"
          onFileSelect={handleResume}
        />

        <JobDescriptionCard
          jobText={jobText}
          setJobText={setJobText}
          onAnalyze={analyze}
        />

      </div>

      {skills.length > 0 && (

        <div className="max-w-6xl mx-auto mt-16">

          <h2 className="text-3xl text-white font-bold mb-8">
            Extracted Skills
          </h2>

          <div className="flex flex-wrap gap-4">

            {skills.map((skill) => (

              <span
                key={skill}
                className="bg-cyan-500 px-4 py-2 rounded-full text-white"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

        

      )}{readiness > 0 && (

  <div className="max-w-6xl mx-auto mt-16">

    <div className="bg-slate-900 rounded-2xl p-8 border border-slate-800">

      <h2 className="text-3xl font-bold text-white mb-8">
        Analysis Results
      </h2>

      <div className="grid md:grid-cols-3 gap-8">

        {/* Readiness */}

        <div className="bg-slate-950 rounded-xl p-6 text-center">

          <h3 className="text-xl text-slate-300">
            Readiness Score
          </h3>

          <div className="text-6xl font-bold text-cyan-400 mt-5">
            {readiness}%
          </div>

        </div>

        {/* Matched */}

        <div className="bg-slate-950 rounded-xl p-6">

          <h3 className="text-xl font-bold text-green-400 mb-4">
            Matched Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {matched.map((skill) => (

              <span
                key={skill}
                className="bg-green-600 px-3 py-2 rounded-full text-white"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

        {/* Missing */}

        <div className="bg-slate-950 rounded-xl p-6">

          <h3 className="text-xl font-bold text-red-400 mb-4">
            Missing Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {missing.map((skill) => (

              <span
                key={skill}
                className="bg-red-600 px-3 py-2 rounded-full text-white"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

      </div>

    </div>

  </div>

)}
{readiness > 0 && (

  <div className="max-w-6xl mx-auto mt-8">

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8 text-center">

      <h2 className="text-3xl font-bold text-white">
        Ready for the Interview?
      </h2>

      <p className="text-slate-400 mt-3">
        Generate AI-powered interview questions based on your Resume and Job Description.
      </p>

      <button
        onClick={generateInterviewQuestions}
        className="mt-8 bg-cyan-500 hover:bg-cyan-600 text-white px-8 py-4 rounded-xl text-lg font-semibold transition"
      >
        Generate Interview Questions
      </button>

    </div>

  </div>

)}{questions.length > 0 && (

<div className="max-w-6xl mx-auto mt-10">

    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8">

        <h2 className="text-3xl font-bold text-white mb-8">

            AI Generated Interview Questions

        </h2>

        <div className="space-y-4">

            {questions.map((question, index) => (

                <div
                    key={index}
                    className="bg-slate-950 border border-slate-700 rounded-xl p-5"
                >

                    <h3 className="text-cyan-400 font-bold mb-2">

                        Question {index + 1}

                    </h3>

                    <p className="text-white">

                        {question}

                    </p>

                </div>

            ))}

        </div>

    </div>

</div>

)}
{questions.length > 0 && (

<div className="max-w-6xl mx-auto mt-10 text-center">

    <button
        className="bg-green-600 hover:bg-green-700 px-10 py-4 rounded-xl text-white text-xl font-bold transition"
        onClick={() => navigate("/interview", {state: {questions}})}
    >

        🎤 Start Mock Interview
        

    </button>

</div>

)}


    </div>

  );

}