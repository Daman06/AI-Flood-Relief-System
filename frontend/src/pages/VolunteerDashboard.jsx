import { useEffect, useState } from "react";

function VolunteerDashboard() {
  const [requests, setRequests] = useState([]);

  const [stats, setStats] = useState({
    total_requests: 0,
    high_priority: 0,
    available_volunteers: 0,
    missions_in_progress: 0,
  });

  const fetchRequests = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/requests");
      const data = await res.json();
      setRequests(data);
    } catch (err) {
      console.log(err);
    }
  };

  const fetchStats = async () => {
    try {
      const res = await fetch("http://127.0.0.1:8000/dashboard-stats");
      const data = await res.json();
      setStats(data);
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    fetchRequests();
    fetchStats();

    const interval = setInterval(() => {
      fetchRequests();
      fetchStats();
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const acceptMission = async (id) => {
    try {
      await fetch(`http://127.0.0.1:8000/accept/${id}`, {
        method: "PUT",
      });

      fetchRequests();
      fetchStats();
    } catch (err) {
      console.log(err);
    }
  };

  const priorityColor = (priority) => {
    switch (priority) {
      case "Critical":
        return "#dc2626";

      case "High":
        return "#ef4444";

      case "Medium":
        return "#f59e0b";

      default:
        return "#22c55e";
    }
  };

  return (
    <div
      style={{
        background: "#eef2ff",
        minHeight: "100vh",
        padding: "30px",
      }}
    >
      <h1
        style={{
          textAlign: "center",
          color: "#1e3a8a",
          marginBottom: "35px",
        }}
      >
        🚑 Volunteer Rescue Dashboard
      </h1>
      <button
      onClick={() => navigate("/")}
      style={{
        marginBottom: "20px",
        background: "#6b7280",
        color: "white",
        border: "none",
        padding: "10px 20px",
        borderRadius: "8px",
        cursor: "pointer",
      }}
    >
      ← Back to Home
    </button>

    <div
      style={{
        display: "grid",
        gridTemplateColumns: "repeat(2, 1fr)",
        gap: "20px",
      }}
    ></div>

     

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4,1fr)",
          gap: "20px",
          marginBottom: "40px",
        }}
      >
        <div className="card">
          <h3>Total Requests</h3>
          <h1>{stats.total_requests}</h1>
        </div>

        <div className="card">
          <h3>High Priority</h3>
          <h1>{stats.high_priority}</h1>
        </div>

        <div className="card">
          <h3>Available Volunteers</h3>
          <h1>{stats.available_volunteers}</h1>
        </div>

        <div className="card">
          <h3>Missions In Progress</h3>
          <h1>{stats.missions_in_progress}</h1>
        </div>
      </div>

      {requests.length === 0 ? (
        <h2 style={{ textAlign: "center" }}>
          No Rescue Requests Available
        </h2>
      ) : (
        requests.map((request) => (
          <div
            key={request._id}
            style={{
              background: "white",
              borderRadius: "18px",
              padding: "25px",
              marginBottom: "25px",
              boxShadow: "0px 5px 18px rgba(0,0,0,.12)",
            }}
          >
            <h2 style={{ color: "#1e3a8a" }}>
              👤 {request.victim_name}
            </h2>

            <hr />

            <p>
              <strong>📞 Phone:</strong> {request.phone_number}
            </p>

            <p>
              <strong>📍 Location:</strong> {request.location}
            </p>

            <p>
              <strong>📝 Emergency:</strong>{" "}
              {request.emergency_message}
            </p>

            <p>
              <strong>🌊 Flood Verified:</strong>{" "}
              {request.flood_verified ? "✅ Yes" : "❌ No"}
            </p>

            <p>
              <strong>⚠ Risk Level:</strong>{" "}
              {request.risk_level}
            </p>

            <p>
              <strong>🚨 Priority:</strong>

              <span
                style={{
                  marginLeft: "10px",
                  background: priorityColor(request.priority),
                  color: "white",
                  padding: "5px 15px",
                  borderRadius: "20px",
                }}
              >
                {request.priority}
              </span>
            </p>

            <p>
              <strong>👨‍🚒 Volunteer:</strong>{" "}
              {request.assigned_volunteer || "Not Assigned"}
            </p>

            

            <p>
              <strong>📌 Status:</strong>{" "}
              {request.mission_status}
            </p>

            {request.latitude && request.longitude && (
              <a
                href={`https://www.google.com/maps?q=${request.latitude},${request.longitude}`}
                target="_blank"
                rel="noreferrer"
                style={{
                  display: "inline-block",
                  marginTop: "10px",
                  color: "#2563eb",
                  textDecoration: "none",
                }}
              >
                📍 Open in Google Maps
              </a>
            )}

            <br />

            {request.mission_status !== "In Progress" && (
              <button
                onClick={() => acceptMission(request._id)}
                style={{
                  marginTop: "20px",
                  background: "#2563eb",
                  color: "white",
                  border: "none",
                  padding: "12px 28px",
                  borderRadius: "10px",
                  cursor: "pointer",
                  fontSize: "16px",
                }}
              >
                Accept Mission
              </button>
            )}
          </div>
        ))
      )}
    </div>
  );
}

export default VolunteerDashboard;