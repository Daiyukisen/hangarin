# 🌸 Hangarin — Personal Task Manager

> **"Hangarin"** is a Filipino word that means to wish, to aspire, or to achieve. This application is built to help you track your goals, manage your daily work, and see your progress clearly in one clean space.

---

## 🚀 Key Features

### 👤 User Account Control
* **Flexible Login:** Securely register or log in using your standard username/password, or connect instantly using your Google or GitHub account.

### 📋 Task Mastery
* **Core Tasks:** Create, edit, and remove main tasks easily. Assign them colors or labels using custom categories and priority levels.
* **Sub-Tasks:** Break large, overwhelming goals down into tiny, actionable checklist steps.
* **Side Notes:** Keep important details, links, or thoughts attached directly to a specific task so you never lose them.

### 📈 Smart Interface
* **Progress Dashboard:** View a simple visual breakdown of your completed tasks over time to stay motivated.
* **Instant Search:** Find any task or note immediately using the quick search feature.
* **Fully Mobile Friendly:** Manage your day from your desktop computer or on the go from your smartphone.

---

## 📊 Technical Blueprint

| System Layer | Selected Technology | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.11 | Core programming language |
| **Framework** | Django 5.0.6 | Backend logic, security, and routing |
| **Authentication** | django-allauth | Handles Google & GitHub secure logins |
| **Database** | SQLite | Local data storage |
| **Frontend** | Bootstrap 5.3 & Font Awesome 6.5 | Clean user interface, buttons, and icons |
| **Hosting** | PythonAnywhere | Cloud deployment platform |

---

## 🛠️ Step-by-Step Installation

Follow these steps to get the project running on your local computer.

### 1. Get the Files
Clone the project from GitHub and move into the project directory:
```bash
git clone [https://github.com/Daiyukisen/hangarin.git](https://github.com/Daiyukisen/hangarin.git)
cd hangarin
```

### 2. Prepare the Virtual Environment

Now, activate it depending on which terminal app you use:

For Git Bash:
```bash
source hangarinenv/Scripts/activate
```

For Command Prompt (CMD):
```bash
hangarinenv\Scripts\activate.bat
```

###3. Load Dependencies & Run
Install the required packages, update your local database tables, and boot up the system:
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## ⚙️ Integrations & App Configuration
To enable the Google and GitHub social login buttons, you must link them to your developer accounts:

### 1. Go to the Django Admin panel at http://127.0.0.1:8000/admin/.

### 2. Find the Social Applications section.

### 3. Add a new application and input your unique Client ID and Secret Key generated from your Google Cloud Console or GitHub Developer Portal.

## 📂 Project Architecture
```bash
📁 Hangarin/ (Root Directory)
 │
 ├── 📁 config/          ➔ Global project configuration, settings, and main URLs
 ├── 📁 hangarin/        ➔ Core application layout and foundational elements
 ├── 📁 taskmanager/     ➔ Database models (Tasks, SubTasks, Notes, Categories)
 ├── 📁 templates/       ➔ HTML file structures for the web pages
 ├── 📁 static/          ➔ Visual design assets (CSS styles, icons, javascript files)
 │
 └── 📄 manage.py        ➔ Main Django command-line tool for migrations and server control
```

## 👩‍💻 Core Developer
Designed by [**Daiyukisen**](https://github.com/Daiyukisen)