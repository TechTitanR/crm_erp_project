# CRM/ERP Flask Web App (PostgreSQL + Render Deployment)

A simple, fully functional **Customer & Order Management (CRM/ERP)** system built using **Flask**, **PostgreSQL (via Render)**, and **SQLAlchemy**.
This app allows you to manage customers, orders, generate reports, and supports CRUD operations with database backups—all deployed on Render with live demo access.

---

## 🚀 Live Demo

🔗 [Live Deployed App on Render](https://crm-erp-project.onrender.com)

---

## ✨ Features

```plaintxt
✅ Dashboard Summary (Total Customers & Orders)
✅ Add / View / Update / Delete Customers
✅ Add / View / Update / Delete Orders (with Customer Dropdown)
✅ Auto PostgreSQL Table Creation on Deploy
✅ Basic Report Generation (Orders Summary)
✅ Error Handling: Custom 404 & 500 Pages
✅ Lightweight, Minimal UI
✅ PostgreSQL (Render) — Production Ready
✅ Render Deployment with Gunicorn
```

---

## 📁 Project Structure

```plaintext
crm_erp_project/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment command (Gunicorn)
├── .gitignore             # Git ignored files
│
├── templates/             # HTML Templates (Jinja2)
│   ├── base.html          
│   ├── dashboard.html     
│   ├── customers.html     
│   ├── orders.html        
│   ├── report.html        
│   ├── 404.html           
│   └── 500.html           
│
├── static/
│   └── style.css          # Custom CSS
│
└── screenshots/           # App Screenshots (For ReadMe)
    ├── dashboard.png
    ├── customers.png
    ├── orders.png
    └── reports.png

```

---

## 💻 Local Development

### 1. Clone the repository:

```bash
git clone https://github.com/TechTitanR/crm_erp_project.git
```
cd crm_erp_project

---

### 2. Create virtual environment:
```bash 
python -m venv venv
```
### On Windows
```bash 
venv\Scripts\activate
```
### On Mac/Linux
```bash
source venv/bin/activate
```
---

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
---

### 4. Run the app:
```bash
python app.py
```
---

### 5. Visit in your browser:
```bash
http://127.0.0.1:5000/
```
---

## ☁️ Deployment on Render
- Push your code to GitHub.
- Log in to Render and create a new Web Service.
- Connect your GitHub repository.
- Add PostgreSQL Service in Render Dashboard
- Set the following settings:

### Build Command:
```bash
pip install -r requirements.txt
```
### Start Command:
```bash
gunicorn app:app
```
## Environment Variable:
- (Optional) Add environment variables if required.
```bash
DATABASE_URL = (provided by Render PostgreSQL)
```
--- 

## 🛠️ Tech Stack
- Backend: Python (Flask)
- Database: PostgreSQL (Render)
- ORM: SQLAlchemy
- Frontend: HTML5, CSS3 (Jinja2)
- Deployment: Render + Gunicorn

---

## 🖼️ Screenshots
- Dashboard
- Customers
- Orders
- Reports

---

## 🙋‍♂️ Author
- Rishi Bakliwal
- rishibakliwaljain@gmail.com

--- 

## 📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.

