````markdown
# Social Media Platform

A social media-like web application where users can create posts, comment, and interact with each other. Built with **Django** for the backend and **React.js** for the frontend.

---

## Features

- User registration and authentication with **JWT**
- Create, read, update, and delete (CRUD) posts
- Comment on posts
- Responsive and modern UI using **Tailwind CSS**
- API communication between frontend and backend with **Axios**
- Data storage with **MongoDB** via **PyMongo**

---

## Tech Stack

**Backend:**
- Django
- JWT for authentication
- PyMongo for database integration
- Python 3.x

**Frontend:**
- React.js
- Tailwind CSS for styling
- Axios for API requests

**Database:**
- MongoDB

---

## Installation

### Backend

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd backend
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Start the Django server:

   ```bash
   python manage.py runserver
   ```

### Frontend

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```
2. Install dependencies:

   ```bash
   npm install
   ```
3. Start the development server:

   ```bash
   npm start
   ```

---

## Usage

* Register or login to the platform
* Create posts, view other users’ posts, and comment
* All actions are updated in real-time using API integration

---

## Learnings

* Full-stack development with **Django + React.js**
* Implementing **JWT authentication**
* Integrating **MongoDB** with Python
* Building responsive and interactive frontends with **Tailwind CSS**

---

## License

This project is for personal learning and portfolio purposes.

```
