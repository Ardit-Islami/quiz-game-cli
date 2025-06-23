def main():
    pass

def start_quiz():

    def generate():
        quiz()
        items = list(dictionary_T.items())
        random_items = random.sample(items, 10)
        random_dict = dict(random_items)
        global final_questions
        final_questions = list(random_dict.keys())
        global correct_answers
        correct_answers = list(random_dict.values())
        root.destroy()
        interface()
    
    root = Tk()
    root.configure(background='#407963')
    root.title('Your favourite Quiz Master')
    root.update_idletasks()                                                          
    screen_width = root.winfo_screenwidth()                                         
    screen_height = root.winfo_screenheight()                                        
    x = (screen_width // 2) - (325 // 2)                                             
    y = (screen_height // 2) - (325 // 2)

    root.geometry(f'325x100+{x}+{y}')

    header = ttk.Label(root, text="Generate your Quiz!", font=("Arial", 24, "bold"), background='#407963', foreground='white')
    header.pack(pady=10)  # Add some vertical padding

    finish = ttk.Button(root, text='Finish', command = generate)
    finish.pack(pady=5)

    root.mainloop()

def quiz():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    url = 'https://quiz-questions.uk/general-knowledge/?utm_content=cmp-true'
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)

    # Find all question elements
    question_elements = driver.find_elements(By.XPATH, '''//p[starts-with(., "1 –") or starts-with(., "2 –") 
                                            or starts-with(., "3 –") or starts-with(., "4 –") 
                                            or starts-with(., "5 –") or starts-with(., "6 –") 
                                            or starts-with(., "7 –") or starts-with(., "8 –") 
                                            or starts-with(., "9 –") or starts-with(., "10 –")]''')

    scraped_questions = []
    answers = []

    for question_text in question_elements:
        scraped_questions.append(question_text.text.split('\n')[0])                                               # The question is the text of the element

        answer_input = question_text.find_element(By.XPATH, './/input[starts-with(@id, "bg-show-less-text-")]')   # The answer is the value of the input tag with id="bg-show-less-text-..."
        answers.append(answer_input.get_attribute('value'))

    driver.quit()

    pattern = re.compile(r'\d+ – ')
    clean_questions = [pattern.sub('', question) for question in scraped_questions]
    print(scraped_questions)
    print(clean_questions)

    global dictionary_T
    dictionary_T = dict(zip(clean_questions, answers))

def interface():
    root = Tk()                                                                                                         # Initialise our new window interface
    root.title('The Quiz Game Project!')

    root.configure(background='#407963')
    root.update_idletasks()                                                                                             # Update the GUI to get the correct dimensions
    screen_width = root.winfo_screenwidth()                                                                             # This would retrieve your display width in my case 2560
    screen_height = root.winfo_screenheight()                                                                           # This would retrieve your display width in my case 1440
    x = (screen_width // 2) - (750 // 2)                                                                                # x-coordinate for the left edge of the window such that the window will be centered horizontally
    y = (screen_height // 2) - (750 // 2)                                                                               # y-coordinate for the top edge of the window such that the window will be centered vertically

    root.geometry(f'750x750+{x}+{y}')

    header = ttk.Label(root, text="Quiz Game", font=("Arial", 24), background='#407963')
    header.pack(pady=10)                                                                                                # Add some vertical padding

                                                                                                                        # Generating our set of questions for tkinter and using pack:
    labels = []
    answer_entries = []
    for i in range(len(final_questions)):
        label = ttk.Label(root, text=final_questions[i], font=("Arial", 12), background='#407963', foreground='#4DA6FF')    # Accessing global list variables set in our scraping function.
        label.pack(pady=5)
        labels.append(label)

        answers = ttk.Entry(root, width = 125)
        answers.pack(pady=5, padx=10)
        answer_entries.append(answers)

    def printer():
        attempts = [ans.get() for ans in answer_entries]
        score = 0

        for attempt, answer in zip(attempts, correct_answers):
            if fuzz.partial_ratio(attempt.lower(),answer.lower()) >= 60: 
                score += 1
            else:
                continue
        
        root.destroy()
        messagebox.showinfo("Congratulations!", f'You scored {(score/10)*100}%!')

    finish = ttk.Button(root, text='Finish', command = printer)
    finish.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    import random
    import regex as re
    from fuzzywuzzy import fuzz
    from tkinter import Tk, Label, Button, messagebox, Frame, BooleanVar
    from tkinter import ttk

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options

    start_quiz()