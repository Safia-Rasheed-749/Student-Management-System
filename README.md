# Student-Management-System
A simple Student Management System built with Django and styled using Tailwind CSS. It supports full CRUD operations—Add, View, Update, Delete student records—with a clean and responsive UI. Ideal for beginners learning Django forms, models, views, and Tailwind integration.
🎓 Student Management System (Django + Tailwind CSS)
This is a mini CRUD-based web application built using Django and styled with Tailwind CSS. It allows users to Add, View, Update, and Delete student records in a clean, responsive interface.

✅ Features
📋 Add New Student with name, email, phone, course, and address

🔍 View All Students in a list format

✏️ Edit Student Details

❌ Delete Student with confirmation

🌐 Responsive UI using Tailwind CSS

🔐 Secure form handling with Django’s CSRF protection

🛠️ Tech Stack
Backend: Django (Python)

Frontend: HTML, Tailwind CSS

Database: SQLite (default Django DB)

Other: Django Forms, Django Messages Framework

📂 Folder Structure (Important Files)
graphql
Copy
Edit
student_management/
├── students/              # Django app with models, views, forms, templates
├── templates/students/    # All HTML templates (add, update, delete, list)
├── static/                # Tailwind CSS and assets
├── db.sqlite3             # SQLite database
├── manage.py              # Django CLI
└── requirements.txt       # Python dependencies
🚀 Setup Instructions
bash
Copy
Edit
git clone https://github.com/your-username/student-management-system.git
cd student-management-system
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
📌 Use Cases
College or university admin panel

Student record-keeping demo

Django beginner’s portfolio project
