#Importing Libraries
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube

import shutil


#Directory Selection
def path_select():
    
    path = filedialog.askdirectory()
    path_label.config(text=path)

def file_download():
    #Get user path
    get_link = link_field.get()
    
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    #Video Downlaod
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    #Move Video to selected Directory
    shutil.move(mp4_video, user_path)
    screen.title('Download Completed Successfully! ')

screen = Tk()
title = screen.title('Youtube Video Downloader')
canvas = Canvas(screen, width=600, height=600)
canvas.pack()

#Image Logo path
image_logo = PhotoImage(file='youtube_image.png')
#Image resizing
image_logo = image_logo.subsample(2, 2)
canvas.create_image(300, 120, image=image_logo)

#Entry Link field
link_field = Entry(screen, width=40, font=('Bahnschrift', 16) )
link_label = Label(screen, text="Enter the Link: ", font=('Bahnschrift', 16))

#Adding to GUI
canvas.create_window(300, 240, window=link_label)
canvas.create_window(300, 280, window=link_field)

#Selecting Path for saving
path_label = Label(screen, text="Choose Path for Download ", font=('Bahnschrift', 16))
select_btn =  Button(screen, text="Select Path", bg='blue', padx='21', pady='4',font=('Bahnschrift', 16), fg='#fff', command=path_select)

#Adding to GUI
canvas.create_window(300, 340, window=path_label)
canvas.create_window(300, 390, window=select_btn)


#Download button
download_btn = Button(screen, text="Download File",bg='green', padx='21', pady='4',font=('Bahnschrift', 16), fg='#fff', command=file_download)
#Adding to GUI
canvas.create_window(300, 450, window=download_btn)

screen.mainloop()