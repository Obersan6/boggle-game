
# Boggle Game

A browser-based word game where users form words from a randomized letter grid. The app checks word validity, tracks scores, and provides live feedback — all powered by Flask and JavaScript.

🎮 [Watch video demo](https://youtu.be/uB6AyBCDPBA)  

---

## 🌟 General Features

- Interactive game interface built with **HTML**, **CSS**, and **JavaScript**
- Real-time word validation using **AJAX** (via Axios)
- **Flask backend** with routes for checking word validity, score submission, and board state
- JSON communication between frontend and backend
- Session-based score and timer tracking
- Responsive and minimal design

---

## 🧱 Tech Stack

- **Backend**: Python, Flask
- **Frontend**: JavaScript, HTML, CSS
- **AJAX**: Axios (for async requests)

---

## 📁 Project Structure

```
flask-boggle/
├── static/
│   ├── index.js           # Main JS logic (gameplay, timer, Axios requests)
│   └── style.css          # Game styling and layout
├── templates/
│   ├── base.html          # Base template
│   └── board.html         # Game board and frontend logic connection
├── app.py                 # Entry point to run the Flask app
├── boggle.py              # Game logic and board generation
├── test_app.py            # Unit tests for app routes
├── words.txt              # Word list used for validation 
└── requirements.txt       # Python dependencies
```

---

## 🚀 Getting Started

### 1. Clone the repo

```
git clone https://github.com/Obersan6/flask-boggle.git
cd flask-boggle
```

### 2. Create a virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run the app

```
flask run
```

Visit `http://localhost:5000` in your browser to play the game.

---

## 🧪 Testing

Run the included test suite:

```
python -m unittest test_app.py
```

---
<!-- 
## 📬 Contact

**Olga Bernal**  
[LinkedIn](https://linkedin.com/in/your-profile) | [Portfolio](https://your-portfolio-link.com)

---

## 📄 License

This project is for educational and portfolio purposes. -->
