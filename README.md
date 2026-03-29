
# 🛡 Women Safety Awareness Chatbot

*A local AI-powered chatbot for women safety guidance using Streamlit + Ollama*

---

## 📌 Overview

This project is a **locally running AI chatbot** designed to provide:

* 🚨 Emergency guidance
* 🧭 Travel safety tips
* 🌐 Online harassment support
* 🥋 Self-defense awareness

It uses:

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM Engine:** Ollama (`phi3` model)

---

## 🎯 Objectives

* Provide **real-time safety awareness**
* Work **offline (no API needed)**
* Be **lightweight and beginner-friendly**
* Demonstrate **AI + UI integration**

---

## 🚀 Features

* 💬 Interactive chatbot UI
* 🧠 AI-powered responses
* 🚨 Emergency detection alerts
* 📌 Sidebar with helpline numbers
* 🔁 Chat memory (context-aware replies)
* ⚡ Local execution (privacy-friendly)

---

## 🏗 Architecture

```text
User → Streamlit UI → Python Backend → Ollama Model → Response → UI
```

### Components

| Layer    | Technology    |
| -------- | ------------- |
| UI       | Streamlit     |
| Logic    | Python        |
| AI Model | Ollama (phi3) |
| Memory   | Session state |

---

## 📁 Project Structure

```text
women-safety-chatbot/
│
├── app.py              # Main application
├── requirements.txt   # Dependencies
├── README.md          # Documentation
└── .gitignore         # Ignored files
```

---

## ⚙️ Prerequisites

Make sure you have:

* Python 3.8+
* pip
* Ollama installed

👉 Install Ollama: [https://ollama.com](https://ollama.com)

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com//Bhavadharani412/women-safety-chatbot.git
cd women-safety-chatbot
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup Ollama Model

```bash
ollama pull phi3
```

(Optional for faster performance)

```bash
ollama pull phi3:mini
```

---

### 5️⃣ Run Application

```bash
streamlit run app.py
```

---

### 6️⃣ Open in Browser

```text
http://localhost:8501
```

---

## 🌐 Access on Other Devices (Same WiFi)

Run:

```bash
streamlit run app.py --server.address 0.0.0.0
```

Then open:

```text
http://<your-ip>:8501
```

---

## 🧠 How It Works

1. User enters query
2. Streamlit captures input
3. Input sent to Ollama model
4. Model generates response
5. Response displayed in UI

---

## 💡 Core Concepts

### 1. Prompt Engineering

Controls chatbot behavior:

```python
SYSTEM_PROMPT = "You are a women safety assistant..."
```

---

### 2. Session Memory

```python
st.session_state.messages
```

Maintains conversation context

---

### 3. AI Integration

```python
ollama.chat(...)
```

Handles response generation

---

## 🚨 Emergency Detection Logic

The chatbot detects danger keywords:

* help
* unsafe
* follow
* attack

Triggers:

```text
🚨 Call 112 immediately
```

---

## 🧪 Testing Guide

### Basic

* What are emergency numbers in India?

### Scenario

* Someone is following me what should I do?

### Stress

* Long emergency situation input

### Failure

* Turn off Ollama → test error handling

---

## ⚡ Performance Optimization

* Use `phi3:mini` model
* Limit chat history
* Reduce response tokens

---

## 🔐 Limitations

* Requires Ollama (local setup)
* Not deployable directly on free cloud
* Performance depends on system hardware

---

## 🚀 Future Improvements

* 🌍 Multilingual support (Tamil, Hindi)
* 🎤 Voice input
* 📍 Location-based help
* ☁️ Cloud deployment (API-based)
* 📱 Mobile app version

---

## 🌐 Deployment Options

| Option          | Status       |
| --------------- | ------------ |
| Local (Ollama)  | ✅ Supported  |
| Streamlit Cloud | ❌ Needs API  |
| Ngrok           | ⚠️ Temporary |
| Hugging Face    | ⚠️ Limited   |

---

## 🤝 Contributing

1. Fork repository
2. Create branch
3. Make changes
4. Submit PR

---

## 📜 License

MIT License

---

## 🙌 Acknowledgements

* Streamlit
* Ollama
* phi3 model

---

## 📌 Key Learning Outcomes

* Build AI-powered apps
* Integrate LLM locally
* Manage session-based memory
* Design safety-focused systems

---
