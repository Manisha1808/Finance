import React, { useEffect, useState } from "react";

function Records({ refresh }) {
  const [records, setRecords] = useState([]);

  const fetchRecords = () => {
    fetch("http://127.0.0.1:5000/records", {
      headers: {
        "User-Id": 2
      }
    })
      .then(res => res.json())
      .then(data => {
        console.log("Records API:", data);
        setRecords(data.data);
      })
      .catch(err => console.log(err));
  };

  useEffect(() => {
    fetchRecords();
  }, [refresh]);

  const handleDelete = (id) => {
    fetch(`http://127.0.0.1:5000/records/${id}`, {
      method: "DELETE",
      headers: {
        "User-Id": 2
      }
    })
      .then(res => res.json())
      .then(() => {
        alert("Deleted!");
        fetchRecords(); // refresh after delete
      });
  };

 return (
  <div className="card">
    <h2 style={{ marginBottom: "20px" }}>All Records</h2>

    <table className="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Amount</th>
          <th>Type</th>
          <th>Category</th>
          <th>Notes</th>
          <th>Action</th>
        </tr>
      </thead>

      <tbody>
        {records.map((r) => (
          <tr key={r.id}>
            <td>{r.id}</td>
            <td>₹ {r.amount}</td>
            <td>{r.type}</td>
            <td>{r.category}</td>
            <td>{r.notes}</td>
            <td>
              <button onClick={() => handleDelete(r.id)}>
                Delete
              </button>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);
}

export default Records;