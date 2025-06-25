# 👤 Flask-Based Profile Web App

---

## 🎯 Objective

To build a **personal profile webpage** using HTML, CSS, and JavaScript, rendered through a **Flask web server**, and containerized using **Docker**. The web page showcases a welcome message, profile photo, a short intro, a contact form, and an interactive "Say Hello" button — all on a **single page**.

---

## 🛠️ Tech Stacks

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3.11 with Flask
- **Web Server**: Flask Development Server
- **Containerization**: Docker
- **IDE/Tools**: VS Code, Docker CLI

---

## 🧩 Steps Included

1. **Set up Flask App**:
   - Created a single Flask route (`/`) to render everything using `render_template_string`.

2. **Designed Profile Page UI**:
   - Added a profile image, welcome heading, and introduction paragraph.
   - Implemented form inputs for Name, Email, and Message.

3. **Added JavaScript Interactivity**:
   - "Say Hello" button prompts the user for their name and greets them using `alert()`.

4. **Styled Using CSS**:
   - Used inline styles for layout, fonts, form, and responsive design.
   - Applied hover effects and consistent spacing for user-friendly UI.

5. **Dockerized the App**:
   - Created `Dockerfile` and `requirements.txt`.
   - Exposed port 5005 and containerized the app using `python app.py`.

---

## 💡 Key Insights

- Using **Flask with `render_template_string()`** helps build small, self-contained apps without external template files.
- Image display in Flask requires placing assets in a **`static/` folder** and referencing them with relative paths.
- Building a Docker image ensures the app runs on any system without worrying about Python environments.
- JavaScript can be seamlessly embedded in server-rendered HTML to provide interactivity (like `prompt()` or `alert()`).
- Proper project structure and documentation make deployment and sharing easier — especially when hosted on GitHub.

---

> ✅ Everything is implemented in a single page as per the project requirement — no sub-navigation, no external routing, and fully Dockerized.
