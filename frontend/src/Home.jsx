import { useNavigate } from "react-router-dom";

function Home() {
  const navigate = useNavigate();

  return (
    <div
      style={{
        height: "100vh",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
        background: "#eef4ff",
      }}
    >
      <div
        style={{
          background: "white",
          padding: "50px",
          borderRadius: "20px",
          textAlign: "center",
          width: "500px",
          boxShadow: "0 8px 25px rgba(0,0,0,.15)",
        }}
      >
        <h1 style={{ color: "#1d4ed8" }}>
          🌊 Flood Relief AI
        </h1>

        <p style={{ marginBottom: "35px" }}>
          AI Powered Disaster Response System
        </p>

        <button
          onClick={() => navigate("/rescue")}
          style={{
            width: "100%",
            padding: "18px",
            marginBottom: "20px",
            background: "#2563eb",
            color: "white",
            border: "none",
            borderRadius: "10px",
            fontSize: "18px",
            cursor: "pointer",
          }}
        >
          🚨 I Need Help
        </button>

        <button
          onClick={() => navigate("/dashboard")}
          style={{
            width: "100%",
            padding: "18px",
            background: "#16a34a",
            color: "white",
            border: "none",
            borderRadius: "10px",
            fontSize: "18px",
            cursor: "pointer",
          }}
        >
          🚑 I'm a Volunteer
        </button>
      </div>
    </div>
  );
}

export default Home;