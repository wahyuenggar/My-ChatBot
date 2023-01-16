#import library yang digunakan
import openai
import tkinter as tk
from tkinter import *

# mengkonfigurasi API key
openai.api_key = "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"

# fungsi chatbot
def chatbot(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n =1,
        stop=None,
        temperature=0.5)

    message = 'Bot :\n' + completions.choices[0].text
    return message

#membuat window GUI
root = Tk()
root.title("My-Chatbot")
root.resizable(False,False)

#deklarasi warna dan font yang digunakan
BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"
FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

#fungsi submit dari tombol GUI untuk send message dan get answer  
def submit():
    prompt = e.get()
    response = chatbot(prompt)
    txt.delete("1.0", tk.END)
    txt.insert(tk.INSERT, response)

#mebuat isi tambilan GUI 
txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, height=10, width=60, padx=10, pady=10)
txt.grid(row=1, column=0, columnspan=2)
 
e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)
 
send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
              command=submit).grid(row=2, column=1)

#menjalankan GUI terus menerus
root.mainloop()
