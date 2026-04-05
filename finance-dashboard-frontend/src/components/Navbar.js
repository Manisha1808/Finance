import React from "react";
import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <div className="navbar">
      <h2 className="logo">💰 Finance</h2>

      <div className="nav-links">
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
    </div>
  );
}

export default Navbar;