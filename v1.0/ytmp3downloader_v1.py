import tkinter as tk
import tkinter.messagebox
from yt_dlp import YoutubeDL
import os
import time

def download():
    global yturl,path,download_msg
    if path.get()=="":
        download_folder = os.path.join(os.path.expanduser("~"), "Downloads") # 下載目標資料夾：Windows 下載資料夾
    else:
        download_folder = download_folder.replace("\\","\\\\")
    url = yturl.get()
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),  #儲存位置與檔名
        'ffmpeg_location': r'C:\ffmpeg\bin',  #ffmpeg 路徑（依照你目前安裝位置）
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }]
        } # yt-dlp 下載參數
    try:  # 開始下載
        label_download_msg.config(fg="red") 
        download_msg.set("下載中...請稍後！") 
        win.update()  # 強制更新 GUI，讓畫面立即顯示「下載中...」
        with YoutubeDL(options) as ydl:
            ydl.download([url])
            #找出下載資料夾中「最新的 mp3」檔案
            mp3_files = [f for f in os.listdir(download_folder) if f.endswith(".mp3")]
            latest_file = max(mp3_files, key=lambda f: os.path.getctime(os.path.join(download_folder, f)))
            latest_path = os.path.join(download_folder, latest_file)
            now = time.time()        #更新時間戳為現在時間
            os.utime(latest_path, (now, now))
            label_download_msg.config(fg="blue")
            download_msg.set("下載完成！")
            print("已下載完成mp3")
    except:
        download_msg.set("")
        if yturl.get()=="":
            tkinter.messagebox.showwarning("無法下載","請輸入YouTube網址")
        else:
            tkinter.messagebox.showwarning("無法下載","無法下載，請確認輸入是否錯誤")

win=tk.Tk()
win.geometry('650x300')
win.title("YTmp3downloader")

label_yturl=tk.Label(win,width=80,text="*YouTube網址 :",font=(20))
label_yturl.place(x=-250,y=50)

label_path=tk.Label(win,width=80,text="       存檔路徑 :",font=(20))
label_path.place(x=-250,y=100)

label_msg=tk.Label(win,width=80,text="(預設為 下載 資料夾)")
label_msg.place(x=-140,y=120)

yturl=tk.StringVar()
entry_yturl=tk.Entry(win,width=60,textvariable=yturl)
entry_yturl.place(x=180,y=52)

path=tk.StringVar()
path.set("")
entry_path=tk.Entry(win,width=60,textvariable=path)
entry_path.place(x=180,y=102)

button_download=tk.Button(win,text="下載影片",command=download)
button_download.place(x=290,y=180)

download_msg=tk.StringVar()
label_download_msg=tk.Label(win,textvariable=download_msg, fg="blue",font="20")
label_download_msg.place(x=295,y=230)
download_msg.set("")

win.mainloop()
