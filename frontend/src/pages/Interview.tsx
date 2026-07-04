import { useState, useEffect, useRef } from "react";
import { useLocation } from "react-router-dom";
import Camera from "../components/Camera";
import { analyzeInterview } from "../services/interviewApi";

const QUESTION_DURATION = 60; // seconds per question

type QuestionResult = {
    question: string;
    transcript?: string;
    fluency_score?: number;
    correctness_score?: number;
    feedback?: string;
    error?: string;
};

type Phase = "loading" | "interviewing" | "analyzing" | "complete";

export default function Interview() {
    const location = useLocation();
    const questions: string[] = location.state?.questions || [];
    const totalQuestions = questions.length || 10;

    const [questionIndex, setQuestionIndex] = useState(0);
    const [timeLeft, setTimeLeft] = useState(QUESTION_DURATION);
    const [phase, setPhase] = useState<Phase>("loading");
    const [results, setResults] = useState<QuestionResult[]>([]);

    const streamRef = useRef<MediaStream | null>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const audioChunksRef = useRef<Blob[]>([]);
    const recordingsRef = useRef<Blob[]>([]);
    const advancingRef = useRef(false); // guards against double-advance (e.g. React StrictMode)

    // Request mic access once when the page loads
    useEffect(() => {
        let cancelled = false;

        (async () => {
            try {
                const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
                if (cancelled) {
                    stream.getTracks().forEach((t) => t.stop());
                    return;
                }
                streamRef.current = stream;
                setPhase("interviewing");
            } catch (err) {
                console.error(err);
                alert("Unable to access microphone. Please allow microphone access and reload.");
            }
        })();

        return () => {
            cancelled = true;
            streamRef.current?.getTracks().forEach((t) => t.stop());
        };
    }, []);

    // Drives the recording + 60s countdown for whichever question is current
    useEffect(() => {
        if (phase !== "interviewing" || !streamRef.current) return;

        advancingRef.current = false;
        setTimeLeft(QUESTION_DURATION);
        startRecording();

        const interval = setInterval(() => {
            setTimeLeft((prev) => {
                if (prev <= 1) {
                    clearInterval(interval);
                    handleQuestionTimeUp();
                    return 0;
                }
                return prev - 1;
            });
        }, 1000);

        return () => clearInterval(interval);
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [questionIndex, phase]);

    const startRecording = () => {
        const stream = streamRef.current;
        if (!stream) return;

        const recorder = new MediaRecorder(stream);
        mediaRecorderRef.current = recorder;
        audioChunksRef.current = [];

        recorder.ondataavailable = (event) => {
            if (event.data.size > 0) audioChunksRef.current.push(event.data);
        };

        recorder.start();
    };

    // Stops the current recorder and resolves with the recorded blob
    const stopRecording = (): Promise<Blob> => {
        return new Promise((resolve) => {
            const recorder = mediaRecorderRef.current;
            if (!recorder || recorder.state === "inactive") {
                resolve(new Blob(audioChunksRef.current, { type: "audio/wav" }));
                return;
            }
            recorder.onstop = () => {
                resolve(new Blob(audioChunksRef.current, { type: "audio/wav" }));
            };
            recorder.stop();
        });
    };

    const handleQuestionTimeUp = async () => {
        if (advancingRef.current) return;
        advancingRef.current = true;

        const blob = await stopRecording();
        recordingsRef.current[questionIndex] = blob;

        if (questionIndex + 1 < totalQuestions) {
            setQuestionIndex((prev) => prev + 1);
        } else {
            // Last question just finished — release the mic and analyze everything
            streamRef.current?.getTracks().forEach((t) => t.stop());
            setPhase("analyzing");
            runAnalysis();
        }
    };

    const runAnalysis = async () => {
        const collected: QuestionResult[] = [];

        // Sequential on purpose: keeps load on the Whisper/XGBoost backend
        // predictable one-answer-at-a-time instead of firing 10 requests at once.
        for (let i = 0; i < totalQuestions; i++) {
            const question = questions[i] || `Question ${i + 1}`;
            const audioBlob = recordingsRef.current[i];

            if (!audioBlob) {
                collected.push({ question, error: "No recording captured for this question." });
                continue;
            }

            try {
                const result = await analyzeInterview(question, audioBlob);
                collected.push({ question, ...result });
            } catch (err) {
                console.error(err);
                collected.push({ question, error: "Analysis failed for this answer." });
            }
        }

        setResults(collected);
        setPhase("complete");
    };

    return (
        <div className="min-h-screen bg-slate-950 p-10">
            <div className="max-w-6xl mx-auto">
                <h1 className="text-5xl font-bold text-white text-center">AI Mock Interview</h1>
                <p className="text-center text-slate-400 mt-4">Practice your interview with AI</p>

                <div className="mt-10 bg-slate-900 rounded-2xl p-8">
                    {phase === "loading" && (
                        <div className="text-center text-slate-300 text-xl py-20">
                            Requesting microphone access...
                        </div>
                    )}

                    {phase === "interviewing" && (
                        <>
                            <div className="flex justify-between items-center">
                                <h2 className="text-cyan-400 text-2xl font-bold">
                                    Question {questionIndex + 1}/{totalQuestions}
                                </h2>
                                <div className="text-red-400 font-bold flex items-center gap-2">
                                    <span className="inline-block w-3 h-3 rounded-full bg-red-500 animate-pulse" />
                                    ⏱ {timeLeft}s
                                </div>
                            </div>

                            {/* Progress Bar */}
                            <div className="mt-6">
                                <div className="w-full h-3 bg-slate-700 rounded-full">
                                    <div
                                        className="h-3 bg-cyan-500 rounded-full transition-all duration-300"
                                        style={{ width: `${(questionIndex / totalQuestions) * 100}%` }}
                                    />
                                </div>
                            </div>

                            {/* Current Question */}
                            <div className="mt-10 bg-slate-950 rounded-xl p-8">
                                <h3 className="text-cyan-400 text-xl font-bold mb-5">Interview Question</h3>
                                <p className="text-white text-xl leading-9">
                                    {questions[questionIndex] || "No question available"}
                                </p>
                            </div>

                            {/* Webcam */}
                            <div className="mt-10 bg-slate-900 rounded-2xl p-8">
                                <h3 className="text-white text-2xl font-bold mb-5">Live Camera</h3>
                                <div className="w-full h-96 bg-black rounded-xl flex items-center justify-center">
                                    <Camera />
                                </div>
                            </div>

                            <div className="mt-10 text-center text-slate-400">
                                🎤 Recording your answer — it will move to the next question automatically when the timer runs out.
                            </div>
                        </>
                    )}

                    {phase === "analyzing" && (
                        <div className="text-center py-20">
                            <h2 className="text-cyan-400 text-2xl font-bold">
                                🤖 AI is analyzing all your answers...
                            </h2>
                            <p className="text-slate-400 mt-4">
                                This may take a minute. Please don't close this page.
                            </p>
                        </div>
                    )}

                    {phase === "complete" && (
                        <div className="space-y-8">
                            <h2 className="text-3xl font-bold text-white mb-4 text-center">Interview Results</h2>

                            {results.map((r, idx) => (
                                <div key={idx} className="bg-slate-950 rounded-2xl p-8">
                                    <h3 className="text-cyan-400 text-lg font-bold mb-3">
                                        Q{idx + 1}. {r.question}
                                    </h3>

                                    {r.error ? (
                                        <p className="text-red-400">{r.error}</p>
                                    ) : (
                                        <div className="space-y-4">
                                            <div>
                                                <h4 className="text-slate-400 font-bold text-sm uppercase">
                                                    Transcript
                                                </h4>
                                                <p className="text-white mt-1">{r.transcript}</p>
                                            </div>
                                            <div className="flex gap-10">
                                                <div>
                                                    <h4 className="text-slate-400 font-bold text-sm uppercase">
                                                        Fluency Score
                                                    </h4>
                                                    <p className="text-white">{r.fluency_score}</p>
                                                </div>
                                                <div>
                                                    <h4 className="text-slate-400 font-bold text-sm uppercase">
                                                        Correctness Score
                                                    </h4>
                                                    <p className="text-white">{r.correctness_score}</p>
                                                </div>
                                            </div>
                                            <div>
                                                <h4 className="text-slate-400 font-bold text-sm uppercase">
                                                    AI Feedback
                                                </h4>
                                                <p className="text-white mt-1">{r.feedback}</p>
                                            </div>
                                        </div>
                                    )}
                                </div>
                            ))}
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}