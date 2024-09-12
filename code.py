import tkinter as tk
from tkinter import messagebox
import random
import string


class GameApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Game Menu")

        tk.Label(root, text="Game Time: Relive Your Childhood",
                 font=("algerian", 24),bg='darkgreen',fg='white').pack(pady=20)

        # Creating buttons for each game
        games = [("Rock-Paper-Scissors", self.rock_paper_scissors),
                 ("Tic-Tac-Toe", self.tic_tac_toe),
                 ("Text Encoding/Decoding", self.text_encoding_decoding),
                 ("Daily Thought", self.daily_thought),
                 ("Treasure Hunt", self.treasure_hunt),
                 ("Dice Rolling Game", self.dice_rolling_game),
                 ("KBC Game", self.kbc_game),
                 ("Make Best Sentence", self.make_best_sentence),
                 ("Movie Guessing Game", self.movie_guessing_game),
                 ("Guessing Mind Number", self.guessing_mind_number),
                 ("Exit", root.quit)]

        for text, command in games:
            tk.Button(root, text=text, command=command,
                      font=("times new roman 20 bold", 14),bg="blue2",fg='white').pack(pady=10)

    def rock_paper_scissors(self):

        def play():
            user_choice = entry_user_choice.get().strip().lower()
            computer_choice = random.choice(['rock', 'paper', 'scissors'])

            if user_choice not in ['rock', 'paper', 'scissors']:
                result_var.set(
                    "Invalid choice. Please choose rock, paper, or scissors.")
                return

            if user_choice == computer_choice:
                result = "It's a tie!"
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                result = "You win!"
            else:
                result = "Computer wins!"

            result_var.set(
                f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}"
            )

        window = tk.Toplevel(self.root)
        window.title("Rock-Paper-Scissors")

        tk.Label(window,
                 text="Enter your choice (rock, paper, or scissors):",
                 font=("Arialbold", 14),bg="blue2",fg="white").pack(pady=10)
        entry_user_choice = tk.Entry(window, font=("Arial", 14 ))
        entry_user_choice.pack(pady=5)

        tk.Button(window, text="Play", command=play,
                  font=("Arial", 14),bg="red",fg="yellow").pack(pady=10)

        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var,
                 font=("Arial", 14)).pack(pady=10)

    def tic_tac_toe(self):

        def check_winner(board, player):
            for i in range(3):
                if all(board[i][j] == player for j in range(3)) or \
                   all(board[j][i] == player for j in range(3)):
                    return True
            if board[0][0] == board[1][1] == board[2][2] == player or \
               board[0][2] == board[1][1] == board[2][0] == player:
                return True
            return False

        def reset_game():
            nonlocal current_player
            for r in range(3):
                for c in range(3):
                    buttons[r][c].config(text='', state='normal')
            current_player = 'X'
            result_var.set("Player X's turn.")

        def button_click(row, col):
            nonlocal current_player
            if board[row][col] == ' ':
                board[row][col] = current_player
                buttons[row][col].config(text=current_player, state='disabled')
                if check_winner(board, current_player):
                    result_var.set(f"Player {current_player} wins!")
                    for r in range(3):
                        for c in range(3):
                            buttons[r][c].config(state='disabled')
                elif all(cell != ' ' for row in board for cell in row):
                    result_var.set("It's a tie!")
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
                    result_var.set(f"Player {current_player}'s turn.")

        window = tk.Toplevel(self.root)
        window.title("Tic-Tac-Toe")

        board = [[' ' for _ in range(3)] for _ in range(3)]
        current_player = 'X'

        buttons = [[None for _ in range(3)] for _ in range(3)]
        for r in range(3):
            for c in range(3):
                buttons[r][c] = tk.Button(
                    window,
                    text='',
                    width=10,
                    height=3,
                    font=("Arial", 24),bg="yellow",fg="black",
                    command=lambda r=r, c=c: button_click(r, c))
                buttons[r][c].grid(row=r, column=c)

        tk.Button(window,
                  text="Reset Game",
                  command=reset_game,
                  font=("Arial", 14)).grid(row=3,
                                           column=0,
                                           columnspan=3,
                                           pady=10)

        result_var = tk.StringVar(window, value="Player X's turn.")
        tk.Label(window, textvariable=result_var,
                 font=("Arial", 14)).grid(row=4,
                                          column=0,
                                          columnspan=3,
                                          pady=10)

    def text_encoding_decoding(self):  # Define the function inside the class

        def encode():
            text = entry_text.get().lower()
            encoded_text = ""
            for char in text:
                if char.isalpha():
                    shift = ord(
                        char
                    ) - 96  # Get the position of the letter (a=1, b=2, ...)
                    shifted_char = chr(
                        96 + ((shift + 2) % 26))  # Shift by 2, wrapping around
                    encoded_text += shifted_char
                else:
                    encoded_text += char
            result_var.set("Encoded text: " + encoded_text)
            copy_button.config(state="normal")

        def decode():
            text = entry_text.get().lower()
            decoded_text = ""
            for char in text:
                if char.isalpha():
                    shift = ord(
                        char
                    ) - 96  # Get the position of the letter (a=1, b=2, ...)
                    shifted_char = chr(
                        96 +
                        ((shift - 2) % 26))  # Shift back by 2, wrapping around
                    decoded_text += shifted_char
                else:
                    decoded_text += char
            result_var.set("Decoded text: " + decoded_text)
            copy_button.config(state="normal")

        def copy_to_clipboard():
            self.root.clipboard_clear()
            self.root.clipboard_append(result_var.get())
            messagebox.showinfo("Copied", "Encoded text copied to clipboard!")

        window = tk.Toplevel(self.root)
        window.title("Text Encoding/Decoding")
        tk.Label(window, text="Enter text:", font=("Arial", 14)).pack(pady=5)
        entry_text = tk.Entry(window, width=50, font=("Arial", 14))
        entry_text.pack(pady=5)
        tk.Button(window, text="Encode", command=encode,
                  font=("Arial", 14)).pack(pady=10)
        tk.Button(window, text="Decode", command=decode,
                  font=("Arial", 14)).pack(pady=10)
        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var,
                 font=("Arial", 14)).pack(pady=10)
        copy_button = tk.Button(window,
                                text="Copy Encoded Text",
                                command=copy_to_clipboard,
                                font=("Arial", 14),
                                state="disabled")
        copy_button.pack(pady=10)

    def daily_thought(self):
        thoughts = [
            "Keep your face always toward the sunshine - and shadows will fall behind you.",
            "The only way to do great work is to love what you do.",
            "Believe you can and you're halfway there.",
            "In the middle of every difficulty lies opportunity.",
            "You are never too old to set another goal or to dream a new dream."
        ]
        window = tk.Toplevel(self.root)
        window.title("Daily Thought")
        tk.Label(window,
                text="Enter time in HH:MM AM/PM format:",
                font=("Arial", 14)).pack(pady=5)
        entry_time = tk.Entry(window, font=("Arial", 14))
        entry_time.pack(pady=5)
        self.thought_var = tk.StringVar(window, value="")
        def display_thought():
            time_input = entry_time.get().strip()
            try:
                time, period = time_input.split()
                hour, minute = map(int, time.split(':'))
                if period.upper() not in ['AM', 'PM']:
                    raise ValueError("Invalid period")
                if hour < 1 or hour > 12 or minute < 0 or minute > 59:
                    raise ValueError("Invalid time")

                # Determine greeting based on the hour and AM/PM
                greeting = ""
                if period.upper() == 'AM':
                    if 5 <= hour < 12:
                        greeting = "Good Morning!"
                    else:
                        greeting = "Good Night!"
                else:  # PM
                    if 12 <= hour < 18:
                        greeting = "Good Afternoon!"
                    elif 18 <= hour < 22:
                        greeting = "Good Evening!"
                    else:
                        greeting = "Good Night!"

                index = (hour * 60 + minute) % len(thoughts)
                self.thought_var.set(f"{greeting}\n\n{thoughts[index]}"
                                         )  # Combine greeting and thought
            except Exception as e:
                self.thought_var.set(f"Error: {e}")
        tk.Button(window,
                text="Get Thought",
                command=display_thought,
                font=("Arial", 14)).pack(pady=10)
        tk.Label(window, textvariable=self.thought_var,
                font=("Arial", 14)).pack(pady=10)


    def treasure_hunt(self):
        def start_game():
            result_var.set("Welcome to the Treasure Hunt!")
            result_var.set("You are a brave adventurer seeking hidden treasure.")
            result_var.set("You find yourself in a dark forest with three paths ahead.")
            result_var.set("Path 1 leads to the mountains, Path 2 leads to the river, and Path 3 leads to the swamp.")
            btn_path1.config(state="normal")
            btn_path2.config(state="normal")
            btn_path3.config(state="normal")

        def choose_path(path):
            if path == '1':
                result_var.set("You climb the mountains and find a beautiful meadow.\nYou discover a small chest with some gold coins.\nCongratulations! You won the game!")
            elif path == '2':
                result_var.set("You follow the river and encounter a fierce monster.\nYou fight bravely but ultimately lose the battle.\nGame over.")
            elif path == '3':
                result_var.set("You venture into the swamp and get lost.\nYou never return from the swamp.\nGame over.")

            # Disable path buttons after making a choice
            btn_path1.config(state="disabled")
            btn_path2.config(state="disabled")
            btn_path3.config(state="disabled")

        window = tk.Toplevel(self.root)
        window.title("Treasure Hunt")

        # Display the game description
        result_var = tk.StringVar()
        result_label = tk.Label(window, textvariable=result_var, font=("Arial", 14), justify="left")
        result_label.pack(pady=10)

        # Path buttons
        btn_path1 = tk.Button(window, text="Choose Path 1", font=("Arial", 14), command=lambda: choose_path('1'))
        btn_path1.pack(pady=5)
        btn_path1.config(state="disabled")

        btn_path2 = tk.Button(window, text="Choose Path 2", font=("Arial", 14), command=lambda: choose_path('2'))
        btn_path2.pack(pady=5)
        btn_path2.config(state="disabled")

        btn_path3 = tk.Button(window, text="Choose Path 3", font=("Arial", 14), command=lambda: choose_path('3'))
        btn_path3.pack(pady=5)
        btn_path3.config(state="disabled")

        # Start Game Button
        start_btn = tk.Button(window, text="Start Game", font=("Arial", 14), command=start_game)
        start_btn.pack(pady=10)


    def dice_rolling_game(self):

        def roll_dice():
            result = random.randint(1, 6)
            result_var.set(f"You rolled a {result}.")

        window = tk.Toplevel(self.root)
        window.title("Dice Rolling Game")

        tk.Button(window,
                  text="Roll Dice",
                  command=roll_dice,
                  font=("Arial", 14)).pack(pady=20)

        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var,
                 font=("Arial", 14)).pack(pady=10)


    import tkinter as tk
    import random

    def kbc_game(self):
        questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "Madrid", "Rome"], "answer": "A"},
            {"question": "What is the smallest prime number?", "options": ["0", "1", "2", "3"], "answer": "C"},
            {"question": "What is the largest planet in our solar system?", "options": ["Jupiter", "Saturn", "Neptune", "Mars"], "answer": "A"},
            {"question": "What is the chemical symbol for gold?", "options": ["Au", "Ag" ,"Cu" ,"fe"   ],"answer": "A" },
            {"question": "What is the largest mammal in the world?", "options": [ "Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],"answer": "B" },
            {"question": "What is the largest organ in the human body?", "options": [ "Heart", "Liver", "Skin", "Brain" ],"answer": "C" },
            {"question": "What is the smallest country in the world as size?", "options": [ "Monaco", "Vatican City", "India","Iraq" ], "answer": "B" },
            {"question": "What is the largest desert in the world?", "options": [ "Sahara", "Gobi", "Antarctica", "Arabian" ], "answer": "C" },
            {"question": "What is the largest bone in the human body?", "options": [ "Femur", "Tibia", "Fibula", "Humerus" ], "answer": "A" },
            {"question": "What is the largest ocean in the world?", "options": [ "Atlantic Ocean" , "Indian Ocean", "Pacific Ocean", "Arctic Ocean"], "answer": "C" },
            {"question": "What is the largest bird in the world?", "options": [ "Ostrich", "Eagle", "Albatross", "Penguin"], "answer": "A" },
            {"question": "What is the largest animal on Earth?", "options": [ "Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "answer": "B" },
            {
              "question": "Who wrote the play 'Romeo and Juliet'?","options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],"answer": "A"
            },
            {
              "question": "In what year did the Titanic sink?",
              "options": ["1912", "1905", "1898", "1920"],
              "answer": "A"},
            {
              "question": "Which famous scientist developed the theory of general relativity?",
              "options": ["Isaac Newton", "Albert Einstein", "Marie Curie", "Niels Bohr"],
              "answer": "B"
            },
            {
              "question": "Which ocean is the deepest on Earth?",
              "options": ["Atlantic Ocean", "Indian Ocean", "Pacific Ocean", "Arctic Ocean"],
              "answer": "C"
            }


            # Add more questions here
        ]

        points = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000,
                  320000, 640000, 1250000, 2500000, 5000000, 70000000]
        level = 0
        current_question = 0
        asked_questions = set()

        def check_answer():
            nonlocal current_question, level
            user_answer = None
            for i, checkbox in enumerate(option_checkboxes):
                if checkbox.get() == 1:
                    user_answer = chr(ord('A') + i)
                    break

            if user_answer == questions[current_question]['answer']:
                level += 1
                result_var.set(f"Correct! Well done! Current Points: {points[level-1]}")
                next_question()
            else:
                result_var.set(f"Incorrect. You won {points[level-1]}.")
                end_game()

        def next_question():
            nonlocal current_question
            if len(asked_questions) >= len(questions):
                result_var.set(f"Congratulations {player_name}! You completed level {level} and won ₹{points[level-1]}!")
                end_game()
                return

            while True:
                current_question = random.randint(0, len(questions) - 1)
                if current_question not in asked_questions:
                    asked_questions.add(current_question)
                    break

            question_label.config(text=questions[current_question]['question'])
            for i, option in enumerate(questions[current_question]['options']):
                option_checkbuttons[i].config(text=f"{chr(ord('A') + i)}. {option}", state="normal")
                option_checkboxes[i].set(0)  # Reset checkboxes
            result_var.set("")
            btn_submit.config(state="normal")  # Enable submit button

        def end_game():
            for checkbox in option_checkbuttons:
                checkbox.config(state="disabled")
            btn_submit.config(state="disabled")
            result_var.set(f"Game Over! {player_name} completed level {level} and won ₹{points[level-1]}!")

        window = tk.Toplevel(self.root)
        window.title("KBC Game")

        tk.Label(window, text="Enter your name:", font=("Arial", 14)).pack(pady=5)
        entry_name = tk.Entry(window, font=("Arial", 14))
        entry_name.pack(pady=5)

        player_name = ""

        def start_game():
            nonlocal player_name
            player_name = entry_name.get().strip()
            if not player_name:
                result_var.set("Please enter your name.")
                return
            entry_name.config(state="disabled")
            next_question()  # Start the game

        tk.Button(window, text="Start", command=start_game, font=("Arial", 14)).pack(pady=10)

        question_label = tk.Label(window, text="", font=("Arial", 14))
        question_label.pack(pady=10)

        option_checkboxes = []
        option_checkbuttons = []
        for i in range(4):
            checkbox_var = tk.IntVar(window)
            checkbox = tk.Checkbutton(window, text="", variable=checkbox_var, font=("Arial", 14))
            checkbox.pack(pady=5)
            option_checkboxes.append(checkbox_var)
            option_checkbuttons.append(checkbox)

        btn_submit = tk.Button(window, text="Submit", command=check_answer, font=("Arial", 14))
        btn_submit.pack(pady=10)
        btn_submit.config(state="disabled")

        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var, font=("Arial", 14)).pack(pady=10)


    def make_best_sentence(self):

        # Define basic lists of nouns and verbs
        nouns = {"adventure", "jungle", "treasure", "river", "forest", "monster"}
        verbs = {"discover", "find", "fight", "explore", "travel", "lose"}

        def generate_random_words():
            word_pool = ["adventure", "discover", "jungle", "brave", "lost", "treasure", "monster", "fight", "river", "forest"]
            random_words.set(", ".join(random.sample(word_pool, 5)))

        def check_best_sentence(sentence):
            words = set(sentence.lower().split())
            has_noun = bool(nouns & words)
            has_verb = bool(verbs & words)

            if has_noun and has_verb:
                return True
            return False

        def generate_sentence():
            words = entry_words.get().split(",")
            words = [word.strip().lower() for word in words]  # Clean up spaces and convert to lowercase
            if len(words) < 2:
                result_var.set("Please enter at least two words.")
                return

            sentence = " ".join(words).capitalize() + "."

            # Check if it's the best sentence
            if check_best_sentence(sentence):
                result_var.set(f"The best sentence is: {sentence}")
            else:
                result_var.set(f"Not the best sentence. Try to include a noun and a verb. Your sentence: {sentence}")

        window = tk.Toplevel(self.root)
        window.title("Make Best Sentence")

        # Random Words Section
        random_words = tk.StringVar(value="Click 'Generate Random Words' to get words!")
        tk.Label(window, text="Random Words:", font=("Arial", 14)).pack(pady=10)
        tk.Label(window, textvariable=random_words, font=("Arial", 12)).pack(pady=5)

        tk.Button(window, text="Generate Random Words", command=generate_random_words, font=("Arial", 14)).pack(pady=10)

        # User Input Section
        tk.Label(window, text="Enter words separated by commas:", font=("Arial", 14)).pack(pady=10)
        entry_words = tk.Entry(window, font=("Arial", 14))
        entry_words.pack(pady=5)

        tk.Button(window, text="Generate Sentence", command=generate_sentence, font=("Arial", 14)).pack(pady=10)

        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var, font=("Arial", 14)).pack(pady=10)


    def movie_guessing_game(self):

        def start_game():
            name = entry_name.get().strip()
            if not name:
                result_var.set("Please enter your name.")
                return

            nonlocal word
            word = random.choice(words)
            word_display.set(" ".join(["_" for _ in word]))

            w.extend(["_" for _ in range(len(word))])
            chances.set(len(word) + 2)
            hint_var.set(f"Hint! : Movie Names.")
            result_var.set(f"{name}, you have {chances.get()} chances")
            btn_guess.config(state="normal")
            entry_letter.config(state="normal")

        def guess_letter():
            l = entry_letter.get().strip().lower()
            entry_letter.delete(0, 'end')
            if not l or len(l) > 1 or not l.isalpha():
                result_var.set(
                    f"Please enter a valid single letter. {chances.get()} chances left."
                )
                return

            if l in word.lower():
                result_var.set("You guessed the right letter!")
                for j in range(len(word)):
                    if l == word[j].lower():
                        w[j] = word[j]  # Preserve original case
            else:
                chances.set(chances.get() - 1)
                result_var.set(f"Wrong guess! {chances.get()} chances left.")

            word_display.set(" ".join(w))
            if "_" not in w:
                result_var.set(f"Congratulations {entry_name.get()}! You've won the game.")
                btn_guess.config(state="disabled")
                entry_letter.config(state="disabled")
            elif chances.get() == 0:
                result_var.set(f"Out of chances! The word was '{word}'.")
                btn_guess.config(state="disabled")
                entry_letter.config(state="disabled")

        window = tk.Toplevel(self.root)
        window.title("Movie Guessing Game")

        tk.Label(window, text="Enter your name:", font=("Arial", 14)).pack(pady=5)
        entry_name = tk.Entry(window, font=("Arial", 14))
        entry_name.pack(pady=5)

        tk.Button(window, text="Start Game", command=start_game, font=("Arial", 14)).pack(pady=10)

        word_display = tk.StringVar(window, value="")
        tk.Label(window, textvariable=word_display, font=("Arial", 24)).pack(pady=10)

        tk.Label(window, text="Enter a letter:", font=("Arial", 14)).pack(pady=5)
        entry_letter = tk.Entry(window, font=("Arial", 14))
        entry_letter.pack(pady=5)
        entry_letter.config(state="disabled")

        btn_guess = tk.Button(window, text="Guess Letter", command=guess_letter, font=("Arial", 14))
        btn_guess.pack(pady=10)
        btn_guess.config(state="disabled")

        hint_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=hint_var, font=("Arial", 14)).pack(pady=10)

        result_var = tk.StringVar(window, value="")
        tk.Label(window, textvariable=result_var, font=("Arial", 14)).pack(pady=10)

        words = [
            "Golmaal Again", "Raaz", "Dangal", "Eye", "Badshah", "Maharaja",
            "Kabir Singh", "Khushi", "Kakuda", "Yodha", "Deadpool",
            "Spiderman", "Time Machine"
        ]
        w = []
        word = ""
        chances = tk.IntVar(window, value=0)


    def guessing_mind_number(self):

        def start_game():
            messagebox.showinfo(
                "Step 1",
                "Think of a number between 1 and 100, then press Enter.")
            step_two()

        def step_two():
            messagebox.showinfo("Step 2", "Now double it and press Enter.")
            step_three()

        def step_three():
            random_addition = random.randint(
                1, 100)  # Computer gives a random number
            messagebox.showinfo(
                "Step 3",
                f"Now add the number {random_addition} and press Enter.")
            step_four(random_addition)

        def step_four(random_addition):
            messagebox.showinfo("Step 4",
                                "Now halve the total and press Enter.")
            step_five(random_addition)

        def step_five(random_addition):
            messagebox.showinfo(
                "Final Step",
                "Now subtract the original number you thought of and press Enter."
            )
            reveal_result(random_addition)

        def reveal_result(random_addition):
            messagebox.showinfo(
                "Result", f"The number you have now is {random_addition / 2}!")

        window = tk.Toplevel(self.root)
        window.title("Think of a Number Game")
        tk.Label(window,
                 text="Follow the instructions to play the game.",
                 font=("Arial", 24)).pack(pady=20)
        tk.Button(window, text="Start", command=start_game,
                  font=("Arial", 24)).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()
