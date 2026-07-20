import "../App.css";
import { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";


function RescueRequest() {
    const navigate = useNavigate();
  const [victimName, setVictimName] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [emergencyMessage, setEmergencyMessage] = useState("");
  const [floodAlert, setFloodAlert] = useState(null);
const [result, setResult] = useState(null);
const [latitude, setLatitude] = useState(null);
const [longitude, setLongitude] = useState(null);
const [city, setCity] = useState("");
const [loadingLocation, setLoadingLocation] = useState(false);
const [showAlert, setShowAlert] = useState(false);
const getLocation = () => {
  setLoadingLocation(true);
  const checkFloodAlert = async (lat, lon) => {
  try {
    const response = await axios.get(
      `https://ai-flood-relief-system.onrender.com/flood-alert?latitude=${lat}&longitude=${lon}`
    );

    setFloodAlert(response.data);
    if (response.data.alert) {
  setShowAlert(true);
}

  } catch (err) {
    console.error(err);
  }
};

  if (!navigator.geolocation) {
    alert("Geolocation is not supported by your browser.");
    return;
  }

  navigator.geolocation.getCurrentPosition (
    async (position) => {
      const latitude = position.coords.latitude;
const longitude = position.coords.longitude;

console.log("Latitude:", latitude);
console.log("Longitude:", longitude);

setLatitude(latitude);
setLongitude(longitude);
checkFloodAlert(latitude, longitude);
try {
  const response = await axios.get(
    `https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat=${latitude}&lon=${longitude}`
  );

  const address = response.data.address;

  const detectedCity =
    address.city ||
    address.town ||
    address.village ||
    address.county ||
    "";

  console.log("Detected City:", detectedCity);

  setCity(detectedCity);

} catch (err) {
  console.error("Reverse geocoding failed:", err);
}

setLoadingLocation(false);
    },
    (error) => {
      console.error(error);
      alert("Unable to fetch your location.");
      setLoadingLocation(false);
    }
  );
};
useEffect(() => {
  getLocation();
}, []);

  const handleSubmit = async () => {
    if (latitude === null || longitude === null) {
    alert("Please detect your location first.");
    return;
  }

  if (city === "") {
    alert("Please wait until the city is detected.");
    return;
  }
  try {
    const response = await axios.post(
      "https://ai-flood-relief-system.onrender.com/rescue",
      {
        victim_name: victimName,
        phone_number: phoneNumber,
        location: city,
latitude: latitude,
longitude: longitude,// Temporary
        emergency_message: emergencyMessage,

        flood_verified: null,
        risk_level:null,
        verification_reason: null,
        priority: null,
        priority_reason: null,
        assigned_volunteer: null,
       
        volunteer_status: null,
        mission_status: null,
      }
    );

  console.log(response.data);

setResult(response.data);
  } catch (error) {
    console.error(error);
    alert("Something went wrong!");
  }
};

  return (
    <div className="container">
      <div className="card">
      <h1>🌊 Flood Relief AI</h1>

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
    alignSelf:"flex-start",
  }}
>
  ← Back to Home
</button>
      

        <p className="subtitle">
          AI Powered Disaster Response System
        </p>

        <input
          type="text"
          placeholder="Enter your name"
          value={victimName}
          onChange={(e) => setVictimName(e.target.value)}
        />

        <input
          type="text"
          placeholder="Phone Number"
          value={phoneNumber}
          onChange={(e) => setPhoneNumber(e.target.value)}
        />

        <textarea
          rows="5"
          placeholder="Describe your emergency..."
          value={emergencyMessage}
          onChange={(e) => setEmergencyMessage(e.target.value)}
        ></textarea>
        <button onClick={getLocation}>
  📍 Detect My Location
</button>
{city && (
  <p>
    <strong>Detected City:</strong> {city}
  </p>
)}


        <button
  onClick={handleSubmit}
  disabled={loadingLocation || latitude === null}
>
  {loadingLocation ? "Detecting Location..." : "🚨 Request Help"}
</button>
        {result && (
  <div className="result-card">
    <h2>✅ Rescue Request Submitted</h2>

    <p>
      <strong>Priority:</strong> {result.priority}
    </p>

    <p>
      <strong>Volunteer:</strong> {result.assigned_volunteer}
    </p>

    
    

    <p>
      <strong>Status:</strong> {result.mission_status}
    </p>
  </div>
)}
{showAlert && (
  <div
    style={{
      position: "fixed",
      top: 0,
      left: 0,
      width: "100%",
      height: "100%",
      background: "rgba(0,0,0,0.5)",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      zIndex: 9999,
    }}
  >
    <div
      style={{
        background: "white",
        padding: "30px",
        borderRadius: "15px",
        width: "400px",
        textAlign: "center",
        boxShadow: "0 10px 30px rgba(0,0,0,0.3)",
      }}
    >
      <h2 style={{ color: "#dc2626" }}>
        ⚠ Flood Alert
      </h2>

      <p>{floodAlert?.message}</p>

      <button
        onClick={() => setShowAlert(false)}
        style={{
          marginTop: "20px",
          background: "#2563eb",
          color: "white",
          border: "none",
          padding: "10px 25px",
          borderRadius: "8px",
          cursor: "pointer",
        }}
      >
        OK
      </button>
    </div>
  </div>
)}
      </div>
    </div>
  );
}

export default RescueRequest;