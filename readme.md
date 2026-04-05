# 💰 Finance Dashboard (Full Stack)

A modern full-stack finance dashboard designed to track financial records and visualize key metrics such as income, expenses, and balance.
It combines a RESTful Flask backend with a React-based frontend, offering role-based access control, dynamic data updates, and an intuitive dashboard experience.

---

## 🚀 Features

### 1. User & Role Management

* Create and manage users
* Assign roles: **Admin, Analyst, Viewer**
* Activate / deactivate users
* Role-based access control using middleware

---

### 2. Financial Records Management

* Create, view, update, delete records

* Fields:

  * Amount
  * Type (income / expense)
  * Category
  * Date
  * Notes

* Filtering & search support

* Pagination for record listing

---

### 3. Dashboard & Analytics

* Total income
* Total expenses
* Net balance
* Category-wise breakdown
* Recent transactions
* **Interactive charts (Chart.js) for visualization**

---

### 4. Frontend (React UI)

* Built a **multi-page React application** using React Router
* Implemented **sidebar-based navigation (SaaS-style layout)**
* Designed clean UI with cards, tables, and forms
* Real-time updates after add/delete operations using state management
* Integrated backend APIs using fetch

---

### 5. Access Control

* **Admin** → Full access
* **Analyst** → View records + dashboard
* **Viewer** → View-only

Implemented using custom middleware (`role_required`)

---

### 6. Validation & Error Handling

* Input validation for records
* Type checking (amount, type)
* Proper error messages
* HTTP status codes (400, 403, 404, 500)

---

### 7. Data Persistence

* SQLite database
* SQLAlchemy ORM

---

## 🛠️ Tech Stack

**Frontend**

* React
* React Router
* Chart.js

**Backend**

* Flask
* SQLAlchemy
* SQLite

---

## 📂 Project Structure

```
finance-dashboard/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── middleware/
│   └── database/
│
├── frontend/
│   ├── src/
│   ├── components/
│   └── App.js
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone <your-repo-url>
cd your-repo-name
```

---

### 2. Backend setup

```
cd backend
python -m venv venv
venv\Scripts\activate
pip install flask flask_sqlalchemy flask_cors
python app.py
```

Backend runs on:

```
http://127.0.0.1:5000/
```

---

### 3. Frontend setup

```
cd frontend
npm install
npm start
```

Frontend runs on:

```
http://localhost:3000/
```

---

## 🔐 API Usage

Every request must include:

```
User-Id: <user_id>
Content-Type: application/json
```

## Output Screenshots
<img width="975" height="465" alt="image" src="https://github.com/user-attachments/assets/789b6d8e-6e0d-4482-bd37-0db33a904de7" />
<img width="975" height="465" alt="image" src="https://github.com/user-attachments/assets/fc3e5894-53de-4c95-96f2-d4bce57b4bab" />
<img width="975" height="472" alt="image" src="https://github.com/user-attachments/assets/9151ba83-6bfd-488b-ace2-a7212dd53fe9" />

---

## 📌 API Endpoints

### 👤 Users

| Method | Endpoint    | Description        |
| ------ | ----------- | ------------------ |
| POST   | /users      | Create user        |
| GET    | /users      | Get all users      |
| PATCH  | /users/<id> | Update role/status |

---

### 💳 Records

| Method | Endpoint      | Description   |
| ------ | ------------- | ------------- |
| POST   | /records      | Create record |
| GET    | /records      | Get records   |
| PUT    | /records/<id> | Update record |
| DELETE | /records/<id> | Delete record |

---

### 📊 Dashboard

| Method | Endpoint            | Description              |
| ------ | ------------------- | ------------------------ |
| GET    | /dashboard/summary  | Income, expense, balance |
| GET    | /dashboard/category | Category-wise totals     |
| GET    | /dashboard/recent   | Recent transactions      |

---

## 🔄 Example Workflow

1. Create Admin user
2. Use Admin (`User-Id: 2`) for all actions
3. Add financial records
4. View dashboard analytics and charts
5. Test role-based restrictions

---

## 🧠 Design Decisions

* Used **Flask + SQLAlchemy** for backend simplicity and scalability

* Implemented **middleware-based RBAC**

* Followed **separation of concerns**:

  * Routes → API layer
  * Services → Business logic
  * Models → Database

* Used **React Router for multi-page frontend navigation**

* Implemented **state-based re-fetching for real-time UI updates**

---

## ⚠️ Assumptions

* Authentication is simulated using headers (`User-Id`)
* SQLite used for simplicity
* Application currently runs locally

---

## ⭐ Future Improvements

* JWT Authentication
* Deployment (Render / Vercel)
* Advanced analytics (pie charts, trends)
* Export reports (CSV/PDF)
* Unit and integration tests

---

## 📌 Key Learnings

* Built a complete full-stack system from backend to UI
* Implemented role-based access control using middleware
* Designed scalable API architecture
* Integrated frontend with backend APIs
* Managed state and real-time UI updates in React
* Created a SaaS-style dashboard layout

---

## 👩‍💻 Author

Manisha Sen
