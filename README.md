# 💡 AI Startup Idea Generator

A modern, minimalist **Streamlit web app** that turns your topic or pain point into **billion-dollar AI startup ideas** — in seconds.


---

## 🚀 Features

- 🧠 Generate 3 unique AI startup ideas based on any topic
- 📂 Select from popular startup categories like HealthTech, FinTech, EdTech, and more
- 🎨 Clean, fast Streamlit UI with emojis and smart formatting
- 💾 Save ideas to local `.txt` files (timestamped automatically)
- 🎈 Streamlit animations (`st.balloons()` & success feedback)
- 🔁 Instant idea regeneration without reload

---

## 🧰 Tech Stack

| Layer        | Technology     |
|--------------|----------------|
| UI Framework | [Streamlit](https://streamlit.io) |
| Language     | Python 3.x     |
| File Handling| `os`, `datetime` |
| Deployment   | Streamlit Cloud *(coming soon)* |

---

## 🧠 How It Works

1. Choose a **startup category** (e.g. AI Tools)
2. Type your **topic/problem** (e.g. remote team burnout)
3. Click **"Generate Startup Ideas"**
4. Get 3 dynamic, emoji-enhanced startup concepts
5. Optionally **save** them as a text file

---

## 📦 Project Structure

ai-startup-generator/
├── app.py                # Main Streamlit app
├── generated/            # Folder where saved ideas go
├── .gitignore
└── README.md

---

## ▶️ Run Locally

---

## ▶️ Run Locally

```bash
git clone https://github.com/Surabhi-Gith/ai-startup-generator.git
cd ai-startup-generator

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

pip install streamlit
streamlit run app.py



