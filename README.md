# 📱 Smartphone Management Web Application

## 🎯 Overview

Ce projet est une application web développée en **PHP, HTML et CSS** qui permet une gestion efficace d'un système d'inventaire de smartphones. Il fournit toutes les **opérations CRUD** (Créer, Lire, Mettre à jour, Supprimer) ainsi qu'un **système d'authentification des utilisateurs** et un contrôle d'accès basé sur les rôles.

---

## 🚀 Features

* 🔐 **User Authentication**

  * Login / Logout system
  * Profile management
  * Role-based access (Admin / User)

* 📱 **Smartphone Management**

  * Add new smartphones
  * View smartphone list
  * View detailed information
  * Update smartphone data
  * Delete smartphones

* 👤 **User Roles**

  * **Admin**: Full access (CRUD operations)
  * **User**: Limited access (view and basic interactions)

* 🎨 **Responsive Interface**

  * Clean and simple UI
  * Accessible on different screen sizes

---

## 🛠️ Technologies Used

* **Backend**: PHP
* **Frontend**: HTML, CSS
* **Database**: MySQL
* **Architecture**: Modular PHP (header, footer, authentication, permissions)

---

## 📂 Project Structure

```
📁 project-root/
│
├── index.php
├── auth.php
├── logout.php
├── profile.php
├── permissions.php
│
├── 📁 smartphones/
│   ├── ajouter_smartphone.php
│   ├── liste_smartphones.php
│   ├── details_smartphone.php
│   ├── modifier_smartphone.php
│   ├── supprimer_smartphone.php
│
├── 📁 includes/
│   ├── header.php
│   ├── footer.php
│
├── 📁 database/
│   ├── schema.sql
│   ├── projet_dev_web.sql
│   ├── update_users_table.php
│
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/smartphone-management-web-app.git
cd smartphone-management-web-app
```

### 2️⃣ Setup Database

* Import `projet_dev_web.sql` into MySQL
* Configure your database connection in PHP files

### 3️⃣ Run the project

* Place the project in your local server (XAMPP / WAMP / MAMP)
* Start Apache & MySQL
* Open in browser:

```
http://localhost/smartphone-management-web-app
```

---

## 📊 Database Design

The system uses a relational database with:

* **Users table** (authentication & roles)
* **Smartphones table** (device management)

---

## 🔒 Security Features

* Session-based authentication
* Role-based access control
* Protected routes using permission checks

---

## 📸 Screenshots (Optional)

*Add screenshots of your application here*

---

## 📈 Possible Improvements

* Add search & filtering functionality
* Implement REST API
* Improve UI with a modern framework (React, Bootstrap)
* Add password hashing & stronger security
* Deploy online (e.g., hosting or cloud)

---

## 👨‍💻 Author

**Oumaro Titans Djiguimde**
Data Engineering & AI Student
Passionate about Data, AI, and Software Development 🚀

---

## ⭐ Conclusion

This project demonstrates:

* Backend development with PHP
* Database design and integration
* Full CRUD implementation
* User authentication & authorization

It represents a solid foundation in **web application development**.

---
