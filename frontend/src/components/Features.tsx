import {
  FileText,
  Brain,
  Camera,
  BarChart3,
  Eye,
  Award,
} from "lucide-react";

const features = [
  {
    icon: <FileText size={40} className="text-cyan-400" />,
    title: "Resume Analysis",
    description: "Extract technical skills automatically from resumes."
  },
  {
    icon: <Brain size={40} className="text-cyan-400" />,
    title: "AI Question Generation",
    description: "Generate personalized interview questions."
  },
  {
    icon: <Camera size={40} className="text-cyan-400" />,
    title: "Live Mock Interview",
    description: "Take a real AI-powered interview using your webcam."
  },
  {
    icon: <Eye size={40} className="text-cyan-400" />,
    title: "Behavior Analysis",
    description: "Track eye contact, posture and head stability."
  },
  {
    icon: <BarChart3 size={40} className="text-cyan-400" />,
    title: "Analytics Dashboard",
    description: "Visualize your interview performance."
  },
  {
    icon: <Award size={40} className="text-cyan-400" />,
    title: "Readiness Score",
    description: "Predict interview readiness using XGBoost."
  }
];

export default function Features() {
  return (
    <section
      id="features"
      className="py-28 px-10 bg-slate-950"
    >
      <h2 className="text-5xl font-bold text-center text-white mb-16">
        Features
      </h2>

      <div className="grid md:grid-cols-3 gap-8 max-w-7xl mx-auto">

        {features.map((feature) => (

          <div
            key={feature.title}
            className="bg-slate-900 border border-slate-800 rounded-2xl p-8 hover:border-cyan-500 transition duration-300"
          >

            {feature.icon}

            <h3 className="text-2xl font-semibold mt-6 text-white">
              {feature.title}
            </h3>

            <p className="text-slate-400 mt-4">
              {feature.description}
            </p>

          </div>

        ))}

      </div>
    </section>
  );
}