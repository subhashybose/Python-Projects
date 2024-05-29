import tkinter as tk
from tkinter import *

from pytube import YouTube
from pytube.innertube import _default_clients

_default_clients["ANDROID_MUSIC"] = _default_clients["ANDROID_CREATOR"]


#yt_video = YouTube("https://www.youtube.com/watch?v=CS7hBHVGWs0")

#yt_file = yt_video.streams.filter(file_extension="mp4").get_by_resolution("720p")
#yt_file.download("E:\\Subhash\\GitHub_Repository\\Python-Projects\\Python_GUI")


def downloadvideo() -> StringVar:
    yt_video = YouTube(fld_ent.get())
    yt_file = yt_video.streams.filter(file_extension="mp4").get_by_resolution(fld_drpdwn.get())
    res = yt_file.download("E:\\Subhash\\GitHub_Repository\\Python-Projects\\Python_GUI")
    print("File Saved: " + res)
    return res


window = tk.Tk()
window.title('Python YouTube Video Downloader')

fld_lbl = tk.Label(text="Enter YouTube Video URL: ")
fld_lbl.pack()
fld_ent = tk.Entry(width=100)
fld_ent.pack()

fld_res_lbl = tk.Label(text="Select Resolution: ")
fld_res_lbl.pack()
fld_drpdwn = StringVar(window)
fld_drpdwn.set('360p')
fld_drpdwn_opts = OptionMenu(window, fld_drpdwn, '360p', '720p', '1080p')
fld_drpdwn_opts.pack()

fld_dwnld = tk.Button(text='Download', width=15, height=3, command=downloadvideo)
fld_dwnld.pack()

window.mainloop()

