# Quiz Game CLI

A beginner Python project designed to take a basic quiz concept up one notch.  
Inspired by [Tech with Tim’s Python projects](https://www.youtube.com/watch?v=8ext9G7xspg), I wanted to apply skills from learning data-focused Python to make the quiz smarter — by scraping real general knowledge questions rather than inventing them myself.

This project combines web scraping, fuzzy string matching, and a basic Tkinter GUI into an interactive command-line quiz experience.

---

## Learning Journey

My goal was to take a beginner project and push it a little further:
- Instead of manually coming up with questions, I applied beginner data skills (scraping, cleaning) to dynamically pull questions from a public site.
- I integrated fuzzy logic to make answer evaluation more forgiving, as a way to experiment with string similarity.
- I combined multiple Python tools (Selenium, fuzzywuzzy, Tkinter) in one project, testing my ability to manage different libraries together.

Through this, I learned:
- How small additions (like scraping real data) can significantly improve a simple project’s functionality.
- The importance of error handling when scraping live data.
- How even basic GUI choices impact usability.
  
---

## Features

- **Web scraping with Selenium:** Dynamically fetches general knowledge questions from a public website.
- **Randomized quizzes:** Each game presents a unique set of 10 questions.
- **Fuzzy matching:** Uses `fuzzywuzzy` to score answers, tolerating small typos or variations.
- **Tkinter GUI:** Displays questions and collects user answers through a simple window interface.

---

## Getting Started

### Requirements

- Python 3.x
- `selenium`
- `fuzzywuzzy`
- `regex`
- ChromeDriver (installed and accessible in your PATH)

*(Tkinter is included with most Python installations.)*

---

### Installation

1. Clone the repo:
```bash
git clone https://github.com/Ardit-Islami/quiz-game-cli.git
cd quiz-game-cli
