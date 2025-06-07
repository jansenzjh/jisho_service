# 🐍 Jisho Microservice

A simple Python microservice using Flask that lets you search Japanese words via the [Jisho.org API](https://jisho.org).

## 📋 Features

- Web interface with a clean UI
- Enter a Japanese word and get definitions from Jisho
- Integrates with a real external API
- Lightweight and beginner-friendly codebase

## 🚀 Demo Flow

1. Visit the home page `/`
2. Enter a Japanese word (e.g., 猫, 勉強, 走る)
3. Submit the form
4. See definitions and example usage from Jisho

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML + CSS
- [Jisho.org API](https://jisho.org/api/v1/search/words)

## 📁 Project Structure

```
jisho_microservice/
├── app.py                 # Main Flask app
├── requirements.txt       # Dependencies
├── templates/             # HTML templates
│   ├── index.html         # Input form page
│   └── result.html        # Result display page
├── static/
│   └── style.css          # Simple styling
```

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/jansenzjh/jisho_service.git
cd jisho_service

# Set up a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Then open your browser and go to:  
**http://localhost:5000**


