import random as rd
import ttkbootstrap as ttk

words = ['python','programming','computer','hangman','yasir']

word = rd.choice(words)
guessed = ['_']*len(word)
tries = 6
score =100
guessed_letter = []

def check_guess():
    global tries 
    global score
    letter =entry.get().lower()
    entry.delete(0,ttk.END)
    if not letter.isalpha() or len(letter) != 1:
        guess_lbl.config(text="⚔ Enter a single letter.")
        return
    if letter in guessed_letter:
        guess_lbl.config(text="🎯 Already Guessed")
        return
    guessed_letter.append(letter)
    if letter in word :
        for i,l in enumerate(word):
            if l == letter:
                guessed[i]=letter
        guess_lbl.config(text=" Correct! Guess")  
    else:
        tries -=1
        score -=10
        guess_lbl.config(text="Wrong! Guess")
        trie_lbl.config(text=f"Tries Left:{tries}  Total Score:{score}")  

    word_lbl.config(text=" ".join(guessed))   

    if "_" not in guessed:
        guess_lbl.config(text="Congratulation You Win!")
        guess_btn.config(state="disabled")    
    elif tries == 0:
        guess_lbl.config(text=f"You Lose! Word was {word}") 
        guess_btn.config(state="disabled")         



game = ttk.Window(themename="minty")
game.title("Hangman Game")
game.iconbitmap("favicon.ico")
game.geometry("600x600")
game.resizable(False,False)
game.withdraw()

title_lbl = ttk.Label(game,text="Welcome to Hangman Game!",font=("Times New Roman",18,"bold")).pack(side="top",pady=10,padx=10,)
 
word_lbl = ttk.Label(game,text=" ".join(guessed),font=("Arial",14,""))
word_lbl.pack(pady=20)

trie_lbl= ttk.Label(text=f"Tries Left:{tries}  Total Score:{score}")
trie_lbl.pack(padx=10)

entry=ttk.Entry(game,font=("Arial",14,""),width=16)
entry.pack(pady=10)
entry.focus()

guess_btn = ttk.Button(game,text="Guess",command=check_guess)
guess_btn.pack(pady=10)

guess_lbl = ttk.Label(game,text="",font=("Times New Roman",12,"bold"))
guess_lbl.pack(pady=10)

ttk.Label(game,text="Developed by Muhammad Yasir with 💖").pack(side="bottom",pady=10,padx=10)
game.update_idletasks()
game.deiconify()
game.mainloop()