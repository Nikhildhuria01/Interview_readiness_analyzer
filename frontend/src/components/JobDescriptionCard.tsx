interface Props {
  jobText: string;
  setJobText: (value: string) => void;
  onAnalyze: () => void;
}

export default function JobDescriptionCard({
  jobText,
  setJobText,
  onAnalyze,
}: Props) {
  return (
    <div className="bg-slate-900 border border-slate-800 rounded-2xl p-8">

      <h2 className="text-2xl font-bold text-white mb-5">
        Job Description
      </h2>

      <textarea
        rows={10}
        value={jobText}
        onChange={(e) => setJobText(e.target.value)}
        placeholder="Paste the Job Description here..."
        className="w-full bg-slate-950 border border-slate-700 rounded-xl p-4 text-white outline-none focus:border-cyan-400 resize-none"
      />

      <button
        onClick={onAnalyze}
        className="mt-6 w-full bg-cyan-500 hover:bg-cyan-600 text-white py-3 rounded-xl"
      >
        Analyze Resume
      </button>

    </div>
  );
}