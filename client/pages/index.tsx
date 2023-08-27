import React, { useEffect, useState } from "react";

function index() {
  const [message, setMessage] = useState("Loading");
  const [solved, setSolved] = useState([]);
  const [username, setUsername] = useState([]);
  const [profile, setProfile] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        // message = 'Loading'
        // once data is retrieved
        // message = data.message
        setMessage(data.message);
        setSolved(data.solved);
        setUsername(data.username);
        setProfile(data.profile);
      });
  }, []);

  return (
    <div>
      <div>{message}</div>

      {username.map((uid, index) => (
        <div key={index}>{uid}</div>
      ))}

      {profile.map((pid, index) => (
        <div key={index}>{pid}</div>
      ))}

      {solved.map((count, index) => (
        <div key={index}>{count}</div>
      ))}
    </div>
  );
}

export default index;