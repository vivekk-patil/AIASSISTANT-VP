# 🤖 AI Personal Assistant

A smart personal assistant web app built with **Flask** and **Groq AI** that can answer your questions and summarize emails instantly.

---

## ✨ Features

- 💬 **Ask Anything** — Get instant answers to any question using LLaMA 3.3 70B
- 📧 **Email Summarizer** — Paste any email and get a 2-3 sentence summary
- ⚡ **Super Fast** — Powered by Groq's ultra-fast inference engine
- 🌐 **Web Interface** — Clean and simple browser-based UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| AI Model | LLaMA 3.3 70B (via Groq) |
| Frontend | HTML, CSS, JavaScript |
| Config | python-dotenv |

---

## 📁 Project Structure

```
AIASSISTANT/
├── main.py              # Flask backend & API routes
├── .env                 # API keys (never commit this!)
├── requirements.txt     # Python dependencies
├── templates/
│   └── index.html       # Frontend UI
└── static/
    └── style.css        # Styling
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-personal-assistant.git
cd ai-personal-assistant
```

### 2. Install Dependencies
```bash
pip install flask groq python-dotenv
```

### 3. Get Your Groq API Key
- Go to [console.groq.com](https://console.groq.com)
- Sign up / Log in
- Create a new API key

### 4. Setup Environment Variables
Create a `.env` file in the root folder:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 5. Run the App
```bash
python main.py
```

Open your browser and go to → `http://localhost:5000`

---

## 🔌 API Endpoints

### `POST /ask`
Ask any question to the AI assistant.

**Request:**
```json
{
  "message": "What is machine learning?"
}
```

**Response:**
```json
{
  "reply": "Machine learning is a subset of AI..."
}
```

---

### `POST /summarize`
Summarize a long email in 2-3 sentences.

**Request:**
```json
{
  "email": "Dear John, I hope this email finds you well..."
}
```

**Response:**
```json
{
  "summary": "The email discusses..."
}
```

---

## ⚙️ Configuration

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |

---

## 📦 Requirements

```
flask
groq
python-dotenv
```

Or install via:
```bash
pip install -r requirements.txt
```

`requirements.txt`:
```
flask==3.1.0
groq==0.13.0
python-dotenv==1.0.0
```

---

## 🔒 Security Notes

- **Never commit your `.env` file** to GitHub
- Add `.env` to your `.gitignore`:
```
.env
__pycache__/
*.pyc
```

---

## 🙌 Acknowledgements

- [Groq](https://groq.com) — For blazing fast AI inference
- [Meta LLaMA](https://llama.meta.com) — For the LLaMA 3.3 model
- [Flask](https://flask.palletsprojects.com) — For the lightweight web framework

---

## 👨‍💻 Author

Made with ❤️ by **Vivek**
