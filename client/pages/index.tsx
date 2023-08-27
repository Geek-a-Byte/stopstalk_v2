import React, { useEffect, useState } from "react";
function LoadingComponent() {
  return (
    <div>
      <p style={{ marginTop:'25px',textAlign: 'center', fontWeight: 'bold', fontSize: '16px' }}>Loading...</p>
      <div>
      <div className="spinner-box">
        <div className="blue-orbit leo">
        </div>
        <div className="green-orbit leo">
        </div>
        <div className="red-orbit leo">
        </div>
        <div className="white-orbit w1 leo">
        </div><div className="white-orbit w2 leo">
        </div><div className="white-orbit w3 leo">
        </div>
      </div>
      {/* You can add a loading spinner or animation here */}
      </div>
    </div>
  );
}

function Index() {
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState([]);
  const [profile, setProfile] = useState([]);

  useEffect(() => {
    fetch("https://stopstalkv2-server.onrender.com/api/home")
      .then((response) => response.json())
      .then((data) => {
        setTotal(data.total_solved);
        setProfile(data.profile);
        setLoading(false); // Set loading to false when data is fetched
      })
      .catch((error) => {
        console.error('Error fetching data:', error);
        setLoading(false);
      });

  }, []);

  return (
    <>
      <main>
        <h1>StopStalk</h1>
        <p className="description">
          Tracking solved counts of DSA problems powered by NextJS and Flask
        </p>
        <hr />
        {
        loading ? (<LoadingComponent />) : (
        <div>
        <p style={{ marginTop: '25px',textAlign: 'center', fontWeight: 'bold', fontSize: '16px' }}>
          Total Solved {total}
        </p>
        <div className="gridContainer">
          {profile.map((link, index) => (
            <>
            <div className="linkItem">
              <div className="pill">
              <img className="imgContainer" src={link['oj']+'.png'} alt=""  />
              </div>
              <div>
              <a target="_blank" href={link['url']}>{link['text']}</a>
              </div>
            <div>
              {link['solve_count']}
            </div>
            </div>
            </>
        ))}
        </div>
        </div>
        )}
      </main>
    </>
  );
}

export default Index;