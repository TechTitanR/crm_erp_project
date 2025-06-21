# CRM/ERP Flask Web App

A simple, lightweight **Customer and Order Management (CRM/ERP)** web application built using **Python Flask**, **SQLite**, and **SQLAlchemy**. This project demonstrates a basic ERP system with CRUD functionalities, a dashboard, reports, and error handling.

## 🚀 Features

✅ **Dashboard Summary**  
✅ **Add / View Customers**  
✅ **Add / View Orders**  
✅ **Basic Report Generation**  
✅ **Custom 404 & 500 Error Pages**  
✅ Minimal UI with Bootstrap  
✅ SQLite for lightweight storage  
✅ Ready for deployment on Render / Heroku  

---

## 🏗️ Project Structure

crm_erp_project/
│
├── app.py # Main Flask application
├── database.db # SQLite Database (ignored in Git)
├── requirements.txt # Python dependencies
├── Procfile # Deployment file (Render/Heroku)
├── .gitignore # Git ignored files
│
├── templates/
│ ├── base.html # Base template
│ ├── dashboard.html # Dashboard
│ ├── customers.html # Customers Page
│ ├── orders.html # Orders Page
│ ├── report.html # Reports Page
│ ├── 404.html # Custom 404 Error Page
│ └── 500.html # Custom 500 Error Page
│
└── static/
└── style.css # Custom styles

---

## 💻 Local Development

1. **Clone the repository:**
```bash
git clone https://github.com/TechTitanR/crm_erp_project.git
```
  cd crm_erp_project

---

2. **Create virtual environment:**
  python -m venv venv
  venv\Scripts\activate   # On Windows
  source venv/bin/activate  # On Mac/Linux

---

3. **Install dependencies:**
  pip install -r requirements.txt

---

4. **Run the app:**
   python app.py

---

5. **Visit:**
 http://127.0.0.1:5000/

---
