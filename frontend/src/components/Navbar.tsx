import { BrainCircuit } from "lucide-react";

function Navbar() {
  return (
    <nav className="w-full fixed top-0 z-50 bg-slate-950/80 backdrop-blur-lg border-b border-slate-800">
      <div className="max-w-7xl mx-auto flex justify-between items-center px-8 py-4">

        <div className="flex items-center gap-3">
          <BrainCircuit className="text-cyan-400" size={34} />
          <h1 className="text-2xl font-bold text-white">
            Interview AI
          </h1>
        </div>

        <div className="flex gap-8 text-slate-300">

          <a href="#features" className="hover:text-cyan-400 transition">
            Features
          </a>

          <a href="#about" className="hover:text-cyan-400 transition">
            About
          </a>

          <a href="#contact" className="hover:text-cyan-400 transition">
            Contact
          </a>

        </div>

      </div>
    </nav>
  );
}

export default Navbar;