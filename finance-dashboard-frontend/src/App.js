import React, { useState } from "react";
import { Routes, Route, NavLink } from "react-router-dom";

import Dashboard from "./components/Dashboard";
import AddRecord from "./components/AddRecord";
import Records from "./components/Records";
import "./App.css";
function App() {
  const [refresh, setRefresh] = useState(false);

  const triggerRefresh = () => {
    setRefresh(!refresh);
  };

  return (
    <div className="layout">

      {/* Sidebar */}
      <div className="sidebar">
        <h2 className="logo">💰 Finance</h2>

        <NavLink to="/" end>
          Dashboard
        </NavLink>

        <NavLink to="/add">
          Add Record
        </NavLink>

        <NavLink to="/records">
          Records
        </NavLink>
      </div>

      {/* Main Content */}
      <div className="main">
        <Routes>
          <Route path="/" element={<Dashboard refresh={refresh} />} />
          <Route path="/add" element={<AddRecord onAdd={triggerRefresh} />} />
          <Route path="/records" element={<Records refresh={refresh} />} />
        </Routes>
      </div>

    </div>
  );
}

export default App;