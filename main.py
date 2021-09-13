import morseTranslator
import tkinter as tk
import pyperclip

translator = morseTranslator.MorseTranslator()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Tkinter Window")
        self.geometry("400x400")
        self.configure(bg="#C4B9B5")

        self.label = tk.Label(self, text="Code Morse Translator", font=("Helvatical bold", 20))
        self.label.configure(bg="#C4B9B5")
        self.label.place(relx=0.5,
                         rely=0.1,
                         anchor='center')

        self.label2 = tk.Label(self,
                               text='Text to convert', font=('normal', 15))

        self.label2.configure(bg='#C4B9B5')
        self.label2.place(relx=0.1,
                          rely=0.3)

        self.input_box = tk.Entry(self)
        self.input_box.place(relx=0.4,
                             rely=0.3,
                             width=200,
                             height=30)

        self.user_entry = self.input_box.get()

        self.button = tk.Button(self, text='ASCII to Morse', command=self.translate_to_morse)
        self.button.place(relx=0.1, rely=0.5, width=110, height=30)

        self.button2 = tk.Button(self, text='Morse to ASCII', command=self.translate_to_ascii)
        self.button2.place(relx=0.5, rely=0.5, width=110, height=30)

        self.button_3 = tk.Button(self, text='Clear', command=self.clear_text)
        self.button_3.place(relx=0.1, rely=0.4, width=110, height=30)

    def clear_text(self):
        self.input_box.delete('0', tk.END)

    def translate_to_morse(self):
        self.user_entry = self.input_box.get()
        pyperclip.copy(translator.text_to_morse(self.user_entry))

    def translate_to_ascii(self):
        self.user_entry = self.input_box.get()
        pyperclip.copy(translator.morse_to_text(self.user_entry))


def start():
    window = Window()
    window.mainloop()


if __name__ == "__main__":
    start()
