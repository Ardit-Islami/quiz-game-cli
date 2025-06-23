# Quiz Game CLI

A beginner Python project that combines web scraping, fuzzy string matching, and a basic Tkinter GUI to create an interactive quiz game.  
Inspired by [Tech with Tim’s Python projects](https://www.youtube.com/watch?v=8ext9G7xspg), I used this as a way to practice combining multiple Python tools into one program.

---

## 📌 Features

- **Web scraping with Selenium:** Dynamically fetches general knowledge questions from a public website.
- **Randomized quizzes:** Each game presents a unique set of 10 questions.
- **Fuzzy matching:** Uses `fuzzywuzzy` to score answers, tolerating small typos or variations.
- **Tkinter GUI:** Displays questions and collects user answers through a simple window interface.

---

## 🚀 Getting Started

### Requirements

- Python 3.x
- `selenium`
- `fuzzywuzzy`
- `regex`
- ChromeDriver (installed and accessible in your PATH)

*(Tkinter is included with most Python installations.)*

---

### Installation

1️⃣ Clone the repo:
```bash
git clone https://github.com/Ardit-Islami/quiz-game-cli.git
cd quiz-game-cli