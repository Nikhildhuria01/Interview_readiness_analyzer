import { useState } from "react";
import { useLocation } from "react-router-dom";

export default function Interview() {

    const location = useLocation();

    const questions: string[] = location.state?.questions || [];

    const [currentQuestion, setCurrentQuestion] = useState(1);

    const totalQuestions = questions.length || 10;

    return (

        <div className="min-h-screen bg-slate-950 p-10">

            <div className="max-w-6xl mx-auto">

                <h1 className="text-5xl font-bold text-white text-center">

                    AI Mock Interview

                </h1>

                <p className="text-center text-slate-400 mt-4">

                    Practice your interview with AI

                </p>

                <div className="mt-10 bg-slate-900 rounded-2xl p-8">

                    <div className="flex justify-between items-center">

                        <h2 className="text-cyan-400 text-2xl font-bold">

                            Question {currentQuestion}/{totalQuestions}

                        </h2>

                        <div className="text-red-400 font-bold">

                            ⏱ 00:00

                        </div>

                    </div>

                    {/* Progress Bar */}

                    <div className="mt-6">

                        <div className="w-full h-3 bg-slate-700 rounded-full">

                            <div
                                className="h-3 bg-cyan-500 rounded-full transition-all duration-300"
                                style={{
                                    width: `${(currentQuestion / totalQuestions) * 100}%`,
                                }}
                            />

                        </div>

                    </div>

                    {/* Current Question */}

                    <div className="mt-10 bg-slate-950 rounded-xl p-8">

                        <h3 className="text-cyan-400 text-xl font-bold mb-5">

                            Interview Question

                        </h3>

                        <p className="text-white text-xl leading-9">

                            {questions[currentQuestion - 1] || "No question available"}

                        </p>

                    </div>

                    {/* Webcam */}

                    <div className="mt-10 bg-slate-900 rounded-2xl p-8">

                        <h3 className="text-white text-2xl font-bold mb-5">

                            Live Camera

                        </h3>

                        <div className="w-full h-96 bg-black rounded-xl flex items-center justify-center">

                            <span className="text-slate-500">

                                Webcam Preview

                            </span>

                        </div>

                    </div>

                    {/* Controls */}

                    <div className="mt-10 flex justify-center gap-6">

                        <button
                            className="bg-green-600 hover:bg-green-700 px-8 py-4 rounded-xl text-white font-bold"
                        >

                            🎤 Start Recording

                        </button>

                        <button
                            className="bg-red-600 hover:bg-red-700 px-8 py-4 rounded-xl text-white font-bold"
                        >

                            ⏹ Stop

                        </button>

                    </div>

                    {/* Next Question */}

                    <div className="mt-10 text-center">

                        <button

                            onClick={() => {

                                if (currentQuestion < totalQuestions) {

                                    setCurrentQuestion(currentQuestion + 1);

                                }

                            }}

                            className="bg-cyan-500 hover:bg-cyan-600 px-8 py-4 rounded-xl text-white font-bold"

                        >

                            Next Question →

                        </button>

                    </div>

                </div>

            </div>

        </div>

    );

}