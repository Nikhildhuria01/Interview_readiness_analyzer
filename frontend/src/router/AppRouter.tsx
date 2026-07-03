import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "../pages/Landing";
import Dashboard from "../pages/Dashboard";
import Resume from "../pages/Resume";
import SkillGap from "../pages/SkillGap";
import Questions from "../pages/Questions";
import Interview from "../pages/Interview";
import Results from "../pages/Results";

function AppRouter() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/resume" element={<Resume />} />
        <Route path="/skill-gap" element={<SkillGap />} />
        <Route path="/questions" element={<Questions />} />
        <Route path="/interview" element={<Interview />} />
        <Route path="/results" element={<Results />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRouter;