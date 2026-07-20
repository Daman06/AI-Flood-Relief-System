import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "./Home";
import RescueRequest from "./pages/RescueRequest";
import VolunteerDashboard from "./pages/VolunteerDashboard";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Home />} />

        <Route path="/rescue" element={<RescueRequest />} />

        <Route path="/dashboard" element={<VolunteerDashboard />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;