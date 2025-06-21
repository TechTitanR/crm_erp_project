# CRM/ERP Flask Web App

A simple, lightweight **Customer and Order Management (CRM/ERP)** web application built using **Python Flask**, **SQLite**, and **SQLAlchemy**.  
This project demonstrates a basic ERP system with CRUD functionalities, a dashboard, reports, error handling, and is fully ready for deployment on **Render**.

---

## 🚀 Features

✅ Dashboard Summary  
✅ Add / View Customers  
✅ Add / View Orders  
✅ Basic Report Generation  
✅ Custom 404 & 500 Error Pages  
✅ Minimal UI with Bootstrap  
✅ SQLite for lightweight storage  
✅ Ready for deployment on Render  

---

## 📁 Project Structure

```plaintext
crm_erp_project/
│
├── app.py                 # Main Flask application
├── database.db            # SQLite Database (ignored in Git)
├── requirements.txt       # Python dependencies
├── Procfile               # Deployment file (Render/Heroku)
├── .gitignore             # Git ignored files
│
├── templates/             # HTML Templates
│   ├── base.html          # Base template
│   ├── dashboard.html     # Dashboard page
│   ├── customers.html     # Customers page
│   ├── orders.html        # Orders page
│   ├── report.html        # Reports page
│   ├── 404.html           # Custom 404 error page
│   └── 500.html           # Custom 500 error page
│
└── static/
    └── style.css          # Custom styles

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
- Set the following settings:

### Build Command:
```bash
pip install -r requirements.txt
```
### Start Command:
```bash
python app.py
```
- (Optional) Add environment variables if required.

## 🛠️ Tech Stack
- Backend: Python, Flask
- Database: SQLite
- Frontend: HTML, CSS (Bootstrap)
- Deployment: Render

### 🔍 Preview
- (Optional: Add your app screenshot here)

/images/demo_screenshot.png

---

## 🙋‍♂️ Author
- Rishi Bakliwal
- rishibakliwaljain@gmail.com

--- 

## 📄 License
- This project is licensed under the MIT License - see the LICENSE file for details.

