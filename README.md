
# 📝 Task Manager Web App

An exploration of a techstack that my client for my capstone project is using.
A fun and interactive Task Manager built with Flask, Jinja2, Bootstrap 5, and JavaScript.

## 🚀 Features

- Add, complete, and delete tasks
- Tasks stored in a SQLite database via SQLAlchemy
- Strikethrough + green style for completed tasks
- Fun confetti animation when marking a task complete 🎉
- Clean and responsive UI using Bootstrap 5

## 🛠 Tech Stack

- **Python + Flask** – backend web framework
- **Jinja2** – templating engine for HTML rendering
- **Bootstrap 5** – responsive styling and layout
- **SQLite + SQLAlchemy** – lightweight database
- **JavaScript** – frontend interactivity (confetti + button animations)

## 📁 Project Structure

```
task-manager/
├── app.py                 # Flask app
├── templates/
│   ├── base.html          # Base layout template
│   ├── index.html         # Main task list view
│   └── add_task.html      # Task form
├── static/
│   ├── css/
│   │   └── styles.css     # Custom styles
│   └── js/
│       └── celebrate.js   # Confetti animation
├── tasks.db               # SQLite database
└── README.md              # This file
```

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install flask flask_sqlalchemy
```

4. **Run the app**

```bash
python app.py
```

5. Visit `http://127.0.0.1:5000` in your browser 🚀
