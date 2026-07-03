import { motion } from "framer-motion";

function Hero() {
  return (
    <section className="min-h-screen flex flex-col items-center justify-center text-center px-6">

      <motion.h1
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="text-7xl font-extrabold text-white"
      >
        AI Interview
      </motion.h1>

      <motion.h1
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="text-7xl font-extrabold text-cyan-400"
      >
        Readiness Analyzer
      </motion.h1>

      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.5 }}
        className="text-slate-300 mt-8 text-xl max-w-2xl"
      >
        Practice AI-powered mock interviews, analyze your communication,
        body language, technical correctness, and predict your interview
        readiness using Machine Learning.
      </motion.p>

      <motion.div
        className="flex gap-5 mt-12"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.8 }}
      >
        <button className="bg-cyan-500 hover:bg-cyan-600 px-8 py-4 rounded-xl text-lg font-semibold text-white transition">
          Start Interview
        </button>

        <button className="border border-cyan-400 px-8 py-4 rounded-xl text-lg text-cyan-400 hover:bg-cyan-400 hover:text-black transition">
          Learn More
        </button>
      </motion.div>

    </section>
  );
}

export default Hero;