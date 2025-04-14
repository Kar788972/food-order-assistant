
# 🧠 Unified Food Order Assistant

A smart food discovery tool that takes a single prompt like:
> "I want 2 cheese pizzas and a Pepsi, delivered to JBR before 9PM"

…and returns the top food options across multiple platforms like Deliveroo, Talabat, and Careem.

---

## 🚀 Features

- 🔍 One-prompt natural language food ordering
- 🤖 GPT-4 powered NLP extraction
- 🍽️ Mock multi-platform results
- ⚙️ API backend with FastAPI
- 💬 User interface via Streamlit

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| NLP | OpenAI GPT-4 (via API) |
| Backend | Python, FastAPI |
| Frontend | Streamlit (lightweight UI) |
| Data | Mock JSON menus |

---

## 🧪 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/food-order-assistant.git
cd food-order-assistant
```

### 2. Setup Backend
- Install dependencies:
```bash
pip install fastapi uvicorn openai
```
- Add your OpenAI API key in the FastAPI script (`openai.api_key = "your-key"`)
- Run backend:
```bash
uvicorn food_ordering_assistant_backend:app --reload
```

### 3. Run Frontend
- Install dependencies:
```bash
pip install streamlit requests
```
- Run Streamlit app:
```bash
streamlit run food_ordering_assistant_ui.py
```

---

## 🧠 Example Prompt
```
I want 2 chicken burgers and fries to Dubai Marina by 8 PM
```

---

## 🧩 Future Plans
- Real-time scraping or API integration
- Auto-ordering via platform APIs
- WhatsApp integration
- Payment & tracking

---

## 👨‍💻 Built By
Karam Al-Askari — [@karamaskari](https://www.linkedin.com/in/karamaskari)
