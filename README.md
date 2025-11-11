# 🚀 Social Circle: Full-Stack Social Media Platform

A modern social media-like web application where users can create posts, comment, and interact with each other. This project is built using a robust **Django REST Framework** backend and a dynamic **React.js** frontend.

---

## ✨ Features

* **User Management:** Registration and authentication secured with **JWT** (JSON Web Tokens).
* **Post Management:** Full Create, Read, Update, and Delete (**CRUD**) functionality for user posts.
* **Interactions:** Ability to comment on posts.
* **Modern UI/UX:** Responsive design and modern styling implemented with **Tailwind CSS**.
* **API Communication:** Seamless data exchange between frontend and backend using **Axios**.
* **Data Storage:** Persistent data storage using a relational database (e.g., SQLite or PostgreSQL) via the **Django ORM**.

---

## 💻 Tech Stack

### Backend (API)
* **Framework:** Django / Django REST Framework
* **Language:** Python 3.x
* **Authentication:** JWT (JSON Web Tokens)
* **Database Integration:** Django ORM

### Frontend
* **Library:** React.js
* **Styling:** Tailwind CSS
* **HTTP Client:** Axios for API requests

### Database
* PostgreSQL (Recommended for production) or SQLite (for local development)

---

## ⚙️ Installation Guide

### Backend Setup

1.  **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # For Linux/macOS
    source venv/bin/activate
    # For Windows (Command Prompt)
    venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    
4.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5.  **Start the Django server:**
    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd ../frontend
    ```
2.  **Install dependencies:**
    ```bash
    npm install
    ```
3.  **Start the development server:**
    ```bash
    npm start
    ```

The application will typically be accessible at `http://localhost:3000`.

---

## 💡 Usage

1.  **Access the Platform:** Open your browser and navigate to the frontend URL.
2.  **Authenticate:** Register a new user or log in using existing credentials.
3.  **Interact:** Create new posts, view other users' content, and engage by adding comments.
4.  **Real-Time Updates:** All actions are reflected immediately via API integration.

---

## 🧠 Key Learnings

* Mastering full-stack development with the **Django + React.js** stack.
* Implementing secure and stateless authentication using **JWT**.
* Working with the **Django ORM** and relational database concepts.
* Building responsive, utility-first frontends with **Tailwind CSS**.

---

## 📜 License

This project is for personal learning and portfolio purposes.
