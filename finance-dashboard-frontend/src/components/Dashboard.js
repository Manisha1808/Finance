import React, { useEffect, useState } from "react";
import Chart from "./Chart";

function Dashboard({ refresh }) {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch("https://finance-sntx.onrender.com/dashboard/summary", {
      headers: {
        "User-Id": "2"
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log("Dashboard:", data);
        setData(data);
      });
  }, [refresh]);

  return (
    <div className="card">
  <h2 style={{ marginBottom: "20px" }}>Dashboard</h2>

  <div className="metrics-container">
    
    <div className="metric income">
      <p>Total Income</p>
      <h3>₹ {data.total_income || 0}</h3>
    </div>

    <div className="metric expense">
      <p>Total Expense</p>
      <h3>₹ {data.total_expense || 0}</h3>
    </div>

    <div className="metric balance">
      <p>Balance</p>
      <h3>₹ {data.balance || 0}</h3>
    </div>

  </div>

  <div style={{ marginTop: "30px", maxWidth: "600px" }}>
    <Chart data={data} />
  </div>
</div>
  );
}

export default Dashboard;