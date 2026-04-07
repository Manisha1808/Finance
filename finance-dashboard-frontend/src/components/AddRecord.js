import React, { useState } from "react";

function AddRecord({ onAdd }) {
  const [form, setForm] = useState({
    amount: "",
    type: "income",
    category: "",
    notes: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("https://finance-sntx.onrender.com/records", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Id": "2"
      },
      body: JSON.stringify({
        ...form,
        amount: Number(form.amount),
        date: new Date().toISOString().split("T")[0]
      })
    })
      .then(res => res.json())
      .then(() => {
        alert("Record added!");
        setForm({
          amount: "",
          type: "income",
          category: "",
          notes: ""
        });
        onAdd();
      })
      .catch(err => console.log(err));
  };

  return (
    <div className="card add-card">
      <h2>➕ Add New Record</h2>

      <p className="subtext">
        Track your income and expenses easily
      </p>

      <form onSubmit={handleSubmit} className="form">

        <input
          type="number"
          name="amount"
          placeholder="Amount (₹)"
          value={form.amount}
          onChange={handleChange}
        />

        <select name="type" value={form.type} onChange={handleChange}>
          <option value="income">Income</option>
          <option value="expense">Expense</option>
        </select>

        <input
          type="text"
          name="category"
          placeholder="Category (e.g. Salary, Food)"
          value={form.category}
          onChange={handleChange}
        />

        <input
          type="text"
          name="notes"
          placeholder="Notes"
          value={form.notes}
          onChange={handleChange}
        />

        <button type="submit">Add Record</button>

      </form>
    </div>
  );
}

export default AddRecord;