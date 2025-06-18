#  Ollama Local Chatbot (Django + Ollama API)

This is a sleek, responsive AI chatbot built using **Django** on the backend and **Ollama's local models** (e.g., `phi3:mini`) for natural language responses. No internet API required — works entirely offline using locally hosted LLMs!

---

##  Features

- Local AI chat powered by Ollama (e.g., `phi3:mini`)
- Django backend with real-time chat handling
- Clean, responsive frontend (HTML, CSS, JS)
- CSRF-protected POST requests
- Easy-to-deploy on local or internal networks

---

##  Tech Stack

- **Backend**: Python 3.11, Django
- **LLM**: Ollama (`phi3:mini`)
- **Frontend**: HTML5, CSS3, Vanilla JS
- **Version Control**: Git + GitHub

---

## Preview

![Chat UI](screenshots/chat-ui.png)

---
## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/HELLO123-ui/ollama-chatbot.git
cd ollama-chatbot

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

ollama run phi3:mini

python manage.py runserver
Built by Aakarsh Agarwal using Python, Django & Ollama.
