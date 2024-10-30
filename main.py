import threading
import tkinter as tk
from datetime import datetime
from tkinter import font
from time import sleep

# Tkinter Logic #
class FakeTerminal:
    def __init__(self, title, font) -> None:
        self.title = title
        self.font = font
        self.create_frame()

    def create_frame(self):
        self.frame = tk.Frame(win, background='#292929', width=800, height=640)
        self.frame.pack_propagate(False)

        label_title = tk.Label(self.frame, font=self.font, text=self.title, bg='#292929', fg='#8fe25c')
        label_title.pack(pady=0)

        self.text_area = tk.Text(self.frame, font=self.font, bg='black', fg='#8fe25c', wrap='word', height=30)
        self.text_area.pack()

        self.text_area.insert(tk.END, f"This is the terminal for {self.title}.\n")
        self.text_area.config(state=tk.DISABLED)

    def update_text(self, new_text):
        def update():
            self.text_area.config(state=tk.NORMAL)
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, new_text)
            self.text_area.config(state=tk.DISABLED)

        win.after(0, update)

# Creating the main window
win = tk.Tk()
win.configure(background='#292929')
win.title("")
win.resizable(False, False)

fira_code = font.Font(family="Fira Code Semibold", size=12)

win.grid_rowconfigure(0, weight=1)
win.grid_columnconfigure(0, weight=1)

fake_term_1 = FakeTerminal(title="", font=fira_code)
fake_term_1.frame.grid(row=1, column=1, padx=10, pady=1)
fake_term_1.update_text("...")

## Placeholder values

a = "Hello world"

# Background update loop 
# Used for dynamic updating the 
# content of each fake terminal
def loop_2():
    while True:
        fake_term_1.update_text(str(a))
        sleep(1)

def thread_loop_2():
    threading.Thread(target=loop_2, daemon=True).start()

def main():
    thread_loop_2()
    win.mainloop()

if __name__ == "__main__":
    main()
