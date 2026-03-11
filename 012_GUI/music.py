import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
import os
import json
import random
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from PIL import Image, ImageTk
import io
import time

pygame.mixer.init()

root = tk.Tk()
root.title("Spotify Style Music Player")
root.geometry("700x550")
root.configure(bg="#121212")

songs = []
current = 0
playing = False

# --------- UI ---------

title = tk.Label(root,text="🎧 Music Player",font=("Arial",22,"bold"),
bg="#121212",fg="white")
title.pack(pady=10)

song_label = tk.Label(root,text="No song playing",
font=("Arial",12),bg="#121212",fg="#bbbbbb")
song_label.pack()

# Album cover
cover_label = tk.Label(root,bg="#121212")
cover_label.pack(pady=10)

# Progress bar
progress = ttk.Scale(root,from_=0,to=100,orient="horizontal",length=400)
progress.pack(pady=10)

time_label = tk.Label(root,text="00:00 / 00:00",
bg="#121212",fg="white")
time_label.pack()

# Playlist
playlist = tk.Listbox(root,width=60,height=8,bg="#181818",fg="white",
selectbackground="#1DB954")
playlist.pack(pady=10)

# --------- Visualizer ---------

canvas = tk.Canvas(root,width=400,height=80,bg="#121212",highlightthickness=0)
canvas.pack()

bars = []
for i in range(30):
    bar = canvas.create_rectangle(i*15,80,i*15+10,80,fill="#1DB954")
    bars.append(bar)

def animate():
    if playing:
        for bar in bars:
            h = random.randint(10,70)
            canvas.coords(bar,canvas.coords(bar)[0],80-h,
                          canvas.coords(bar)[2],80)
    root.after(100,animate)

animate()

# --------- Functions ---------

def load_music():
    global songs
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files","*.mp3")])
    songs = list(files)

    playlist.delete(0,tk.END)
    for s in songs:
        playlist.insert(tk.END,os.path.basename(s))

def play_music():
    global current,playing

    if playlist.curselection():
        current = playlist.curselection()[0]

    song = songs[current]

    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    playing = True

    song_label.config(text=os.path.basename(song))

    show_cover(song)
    update_progress(song)

def pause_music():
    pygame.mixer.music.pause()

def resume_music():
    pygame.mixer.music.unpause()

def next_song():
    global current
    current += 1
    if current >= len(songs):
        current = 0
    playlist.selection_clear(0,tk.END)
    playlist.selection_set(current)
    play_music()

def prev_song():
    global current
    current -= 1
    if current < 0:
        current = len(songs)-1
    playlist.selection_clear(0,tk.END)
    playlist.selection_set(current)
    play_music()

# --------- Album Cover ---------

def show_cover(song):
    try:
        tags = ID3(song)
        for tag in tags.values():
            if tag.FrameID == "APIC":
                img = Image.open(io.BytesIO(tag.data))
                img = img.resize((200,200))
                img = ImageTk.PhotoImage(img)
                cover_label.config(image=img)
                cover_label.image = img
                return
    except:
        cover_label.config(image="")

# --------- Progress ---------

def update_progress(song):

    audio = MP3(song)
    total = int(audio.info.length)

    def run():
        if playing:
            pos = pygame.mixer.music.get_pos()/1000
            progress.set((pos/total)*100)

            cur = time.strftime("%M:%S",time.gmtime(pos))
            tot = time.strftime("%M:%S",time.gmtime(total))
            time_label.config(text=f"{cur} / {tot}")

        root.after(1000,run)

    run()

# -------- Save Playlist --------

def save_playlist():
    with open("playlist.json","w") as f:
        json.dump(songs,f)

def load_playlist():
    global songs
    try:
        with open("playlist.json") as f:
            songs = json.load(f)

        playlist.delete(0,tk.END)
        for s in songs:
            playlist.insert(tk.END,os.path.basename(s))
    except:
        pass

# -------- Buttons --------

controls = tk.Frame(root,bg="#121212")
controls.pack(pady=15)

def hover(btn):
    btn.bind("<Enter>",lambda e:btn.config(bg="#1DB954"))
    btn.bind("<Leave>",lambda e:btn.config(bg="#282828"))

def make_btn(text,cmd,col):
    b = tk.Button(controls,text=text,command=cmd,
    bg="#282828",fg="white",width=8,font=("Arial",10,"bold"),
    relief="flat")
    b.grid(row=0,column=col,padx=5)
    hover(b)

make_btn("Load",load_music,0)
make_btn("Play",play_music,1)
make_btn("Pause",pause_music,2)
make_btn("Resume",resume_music,3)
make_btn("Prev",prev_song,4)
make_btn("Next",next_song,5)
make_btn("Save",save_playlist,6)
make_btn("Open",load_playlist,7)

root.mainloop()