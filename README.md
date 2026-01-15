# 📘 Employee Management REST API

**HabotConnect Hiring Project**

A secure **Django REST Framework** based Employee Management System implementing **CRUD operations**, **JWT authentication**, **pagination**, **filtering**, and **admin management**, built following **RESTful best practices**.

---

## 🚀 Project Overview

This project provides a backend REST API to manage employees in a company.
It supports creating, viewing, updating, and deleting employee records securely using **JWT-based authentication**.

The project was developed as part of the **HabotConnect Python Backend Developer Hiring Assignment**.

---

## 🧰 Tech Stack

* **Python 3.12**
* **Django**
* **Django REST Framework**
* **JWT Authentication (SimpleJWT)**
* **SQLite (default DB)**
* **Postman (API Testing)**

---

## 📁 Project Structure

```
employee_api/
│
├── employee_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── employees/
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-api.git
cd employee-management-api
```

---

### 2️⃣ Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Create Superuser (For Admin & JWT)

```bash
python manage.py createsuperuser
```

---

### 6️⃣ Run Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

---

## 🔐 Authentication (JWT)

### Get Token

**POST**

```
/api/token/
```

**Body**

```json
{
  "username": "admin",
  "password": "admin123"
}
```

**Response**

```json
{
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN"
}
```

➡️ Use the **access token** as:

```
Authorization: Bearer <token>
```

---

## 📌 API Endpoints

### ➕ Create Employee

**POST**

```
/api/employees/
```

```json
{
  "name": "Ajay Verma",
  "email": "ajay@habot.com",
  "department": "Engineering",
  "role": "Developer"
}
```

✅ `201 Created`

---

### 📄 List Employees (Pagination + Filtering)

**GET**

```
/api/employees/?department=HR&role=Manager&page=1
```

---

### 🔍 Retrieve Single Employee

**GET**

```
/api/employees/{id}/
```

---

### ✏️ Update Employee

**PUT**

```
/api/employees/{id}/
```

---

### ❌ Delete Employee

**DELETE**

```
/api/employees/{id}/
```

✅ `204 No Content`

---

## 🧪 Validation & Error Handling

* ❌ Duplicate email → `400 Bad Request`
* ❌ Empty name → Validation error
* ❌ Invalid ID → `404 Not Found`
* ❌ Unauthorized access → `401 Unauthorized`

---

## 📊 Pagination

* Default page size: **10 records**
* Example:

```
/api/employees/?page=2
```

---

## 🧠 Filtering Support

* By department:

```
/api/employees/?department=Engineering
```

* By role:

```
/api/employees/?role=Developer
```

---

## 🛠️ Django Admin Panel

Access:

```
http://127.0.0.1:8000/admin/
```

Features:

* View employee table
* Search by name/email
* Filter by department/role
* Add/update/delete employees

---

## 🧪 Testing

Basic API tests are written using **Django APITestCase**.

Run tests:

```bash
python manage.py test
```

---

## 📄 Project Documentation

* **Postman Collection** used for API testing
* **Project PDF** included for submission
* Code follows **clean architecture and REST principles**

---

## ✅ Conclusion

This project demonstrates:

* Secure API design
* Proper RESTful architecture
* Token-based authentication
* Clean Django app structure
* Real-world backend development practices

---

Just tell me 👍
