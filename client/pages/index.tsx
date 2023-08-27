import React, { useEffect, useState } from "react";

function index() {
  const [total, setTotal] = useState([]);
  const [profile, setProfile] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8080/api/home")
      .then((response) => response.json())
      .then((data) => {
        setTotal(data.total_solved);
        setProfile(data.profile);
      });
  }, []);

  const solveStyle = {
    fontWeight: 'bold',
    fontSize: '18px'
  };

  return (
    <>
      <main>
        <h1>StopStalk</h1>
        <p className="description">
          Tracking solved counts of DSA problems powered by NextJS and Flask
        </p>
        <hr />
        <p style={solveStyle}>
          Total Solved {total}
        </p>
        <div className="gridContainer">
          {profile.map((link, index) => (
            <>
            <div className="linkItem">
              <div className="pill">
              
            <img className="imgContainer" src={link['oj']+'.png'} alt=""  />
            <div>
            <a target="_blank" href={link['url']}>{link['text']}</a>
            </div>
              </div>
            
            <div>
              {link['solve_count']}
            </div>
            </div>
            
            </>
        ))}
        </div>
      </main>
    <div>
    </div>
    </>
  );
}

export default index;