import random
import threading
import time
from tkinter import *
from random import randint
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Load the audio file
pygame.mixer.music.load("C:\\Users\\Aiman Shariff\\OneDrive\\Desktop\\you-are-an-idiot.mp3")  # Replace "your_audio_file.mp3" with the path to your audio file

root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

# Play the background audio
pygame.mixer.music.play(-1)  # -1 plays the music in an infinite loop


def place_windows():
    while True:
        win = Toplevel(root)
        win.geometry("300x60+0" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(
            randint(0, root.winfo_screenheight() - 60)))
        Label(win, text="You are an idiot", fg="green").place(relx=0.39, rely=0.3)

        win.lift()
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        root.lift()
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        time.sleep(0.05)


threading.Thread(target=place_windows).start()
root.mainloop()
