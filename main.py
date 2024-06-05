from tkinter import *
import os
import random
import time
import threading
from style import blue, yellow, font_type

def play_music():
    while True:
        music_files = get_music_files()
        if not music_files:
            print("No music files found.")
            break
        shuffled_music = random.choice(music_files)
        shuffled_music_full_path = os.path.join(os.curdir, "files", shuffled_music)
        print(f"Playing {shuffled_music_full_path}")
        os.startfile(shuffled_music_full_path)
        time.sleep(5)

def get_music_files():
    try:
        files = os.listdir("files")
        return [f for f in files if f.endswith(".mp3")]  # Filter for .mp3 files
    except Exception as e:
        print(f"Error reading directory: {e}")
        return []

def start_playing_music():
    threading.Thread(target=play_music, daemon=True).start()

root = Tk()
root.configure(bg=blue)
root.geometry("480x320")

title = Label(root, text="Music Program", 
              fg=yellow, 
              bg=blue, 
              font=(font_type, 32))
title.pack()

secondary_title = Label(root, text="Click the button to start music", 
                        fg=yellow, 
                        bg=blue, 
                        font=(font_type, 18))
secondary_title.pack()

run_music_button = Button(root, text="Play music",
                          command=start_playing_music,
                          fg=yellow, bg=blue, 
                          font=(font_type, 18))
run_music_button.pack(side=BOTTOM)

root.mainloop()
