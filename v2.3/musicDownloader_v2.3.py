#---------v2.3---------#

# 處理yt網址出現&list=...會把整個播放清單都下載的問題 (v1.1)
# 會找到出現"&"的索引 並只取其索引前的網址作為下載用的網址(只下載1個檔案) (v1.1)

# 優化UI 新增按鍵: 選擇 開啟資料夾 清除 貼上url (v2.3)
# 新增進度條 (v2.3)
# 用Thread寫 避免視窗"沒有回應" (v2.3)
# 把 ffmpeg/bin 資料夾複製成 ffmpeg_bin 放在cwd資料夾底下 (提高可攜性) (v2.3)

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
import tkinter.filedialog

from yt_dlp import YoutubeDL
import os
import sys
import time

from threading import Thread

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS  # PyInstaller 虛擬資料夾
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def download():
    progress_var.set(0)
    progress_msg.set('準備開始下載...')
    url = yturl.get()
    t = Thread(target=download_task, args=(url,), daemon=True)
    t.start()

def download_task(_url):
    url = _url
    index=url.find("&")  #v1.1新增
    if index != -1:  #v1.1新增
        url=url[:index]  #v1.1新增
        print(f"New url(singal file) is : {url}")  #v1.1新增

    options = { # yt-dlp 下載參數
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  # 儲存位置與檔名
        'ffmpeg_location': resource_path('ffmpeg_bin'),  # ffmpeg 路徑
        'progress_hooks': [progress_hook],   # 進度條
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
        }
    
    try:
        with YoutubeDL(options) as ydl:
            ydl.download([url])

            # 找出下載資料夾中最新的mp3檔案
            mp3_files = [f for f in os.listdir(download_folder) if f.endswith(".mp3")]
            latest_file = max(mp3_files, key=lambda f: os.path.getctime(os.path.join(download_folder, f)))
            latest_path = os.path.join(download_folder, latest_file)
            now = time.time()   # 更新時間戳為現在時間
            os.utime(latest_path, (now, now))
            print("已下載完成mp3")
            win.after(0, actually_done)
    
    except Exception as e:
        print(f'ERROR! {e}')
        win.after(0, on_download_error)

def actually_done():
    progress_var.set(100)
    progress_msg.set("下載完成")

def on_download_error():
    progress_msg.set('')
    if yturl.get()=="":
        tkinter.messagebox.showwarning("無法下載","請輸入YouTube網址")
    else:
        tkinter.messagebox.showwarning("無法下載","無法下載，請確認輸入是否錯誤")

def download_finished_ui():
    progress_var.set(99)
    progress_msg.set("99%   ")

def update_progress(percent):
    if (int(percent) < 100) and (percent > progress_var.get()):
        # print(percent > progress_var.get())
        progress_var.set(percent)
        progress_msg.set(f"{int(percent)}%  ")

def clear_url():
    yturl.set("")

def paste_url():
    try:
        text = win.clipboard_get()   # 從系統剪貼簿取得文字
        yturl.set(yturl.get() + text)   # 貼到 URL 輸入框
    except tk.TclError:
        pass   # 剪貼簿是空的或不是文字

def progress_hook(d): # 進度條

    if d['status'] == 'downloading':
        total = d.get('total_bytes') or d.get('total_bytes_estimate')
        downloaded = d.get('downloaded_bytes')

        if total and downloaded:
            percent = downloaded / total * 100
            
            win.after(0, update_progress, percent)

    elif d['status'] == 'finished':
        win.after(0, download_finished_ui)
 
def select_dir():
    global download_folder
    dir = tkinter.filedialog.askdirectory(title="選擇目標資料夾")
    if dir:
        download_folder = dir
        if len(dir) > 28:
            show_path.set('...' + dir[-26:])
        else:
            show_path.set(dir)

def open_dir():
    os.startfile(download_folder)

win=tk.Tk()
win.geometry('620x275')
win.title("MusicDownloader")
win.resizable(False, False)

label_yturl=tk.Label(win,text = "YouTube網址 :", font = (20))
label_yturl.place(x=50,y=50)

label_path=tk.Label(win, text = "存檔路徑 :",font = (20))
label_path.place(x=50,y=100)

yturl=tk.StringVar()
entry_yturl=tk.Entry(win,width=43,textvariable=yturl)
entry_yturl.place(x=160,y=52)

button_clear = tk.Button(win, text="清除", command=clear_url)
button_clear.place(x=471, y=48)

button_psate = tk.Button(win, text = '貼上', command = paste_url)
button_psate.place(x = 510, y = 48)

download_folder = os.path.join(os.path.expanduser("~"), "Downloads") # 預設下載目標資料夾：Windows 下載資料夾
show_path = tk.StringVar()
show_path.set(download_folder)
label_path=tk.Label(win, textvariable = show_path, font = (20))
label_path.place(x = 130,y = 100)

button_select = tk.Button(win, text = "選擇", command = select_dir)
button_select.place(x = 435, y = 100)

button_open = tk.Button(win, text = "開啟資料夾", command = open_dir)
button_open.place(x = 474, y = 100)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(win, variable=progress_var, maximum=100, length=350)
progress_bar.place(x=130, y=140)

progress_msg = tk.StringVar()
progress_msg.set('')
label_progress = tk.Label(win, textvariable = progress_msg, font = '18')
label_progress.place(x=485, y=140)

button_download=tk.Button(win,text="下載影片",command=download)
button_download.place(x=290,y=190)

win.mainloop()