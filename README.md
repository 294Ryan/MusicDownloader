◽️[中文](#音樂下載器)    ◽️[English](#music-downloader)

# ***音樂下載器***

## **📜目錄**
- [專案概述](#專案概述)
- [重點特色](#重點特色)
- [使用說明](#使用說明)
- [開發須知](#開發須知)
- [使用技術](#使用技術)
- [專案結構](#專案結構)
- [備註](#備註)


## **✏️專案概述**
Tkinter GUI應用程式，下載YouTube影片並自動轉檔成`.mp3`。


## **✨重點特色**
- **簡潔的GUI**介面，易於使用
- 自動**裁剪URL**，僅下載當前影片音訊，而非整個播放清單
- 可自訂下載目的資料夾
- 下載指定連結的YouTube影片並**自動轉檔**成`.mp3`檔案
- 支援一鍵**貼上/清除**URL填寫框
- 下載時顯示**進度條**
- `.exe`執行檔**內置`ffmpeg`工具**，無需額外下載其他工具


## **✅️使用說明**
請先下載Release的內容
- 啟動: 執行`musicDownloader_v2.4.exe`
- 功能介紹:

1. *輸入YT影片URL:*
    於`YouTube網址`輸入框輸入網址，或點選右方的`貼上`鍵直接從剪貼簿貼上。

2. *指定下載目的資料夾:*
    存檔路徑預設為電腦的`下載`資料夾。
    點選視窗中間右側的`選擇`鍵可自選電腦內的指定資料夾為目的資料夾。
    點選`開啟資料夾`鍵自動開啟指定或預設之目的資料夾。

3. *開始下載:*
   點選視窗中的`下載影片`鍵會分配一執行緒執行下載影片之任務，並將其轉檔成`.mp3`檔案，存放在指定或預設的目的資料夾。
   下載過程中會依序出現 *準備開始下載* *下載進度* *下載完成* 等提示內容。
   若網址輸入有誤，會跳出 *無法下載* 的警告提示框，請依照提示重新輸入網址並再試一次。


## **💻開發須知**
1. 請先閱讀下述開發規範
2. 複製此倉庫至本地電腦:
```
cd 目錄
git clone github.com/294Ryan/MusicDownloader.git
```
3. 使用語言:
   - Python 3.13

4. 安裝必要工具:
   - Python模組: 請運行以下指令
     ```
     pip install -r requirements.txt
     ```
   - FFmpeg: 請至<https://share.google/977WgCDSa2UqLznsR>下載，或將倉庫中的`ffmpeg_bin.zip`解壓縮，取得`ffmpeg_bin`資料夾並放置於專案根目錄下。
5. 使用技術: 請參見[使用技術](#🛠使用技術)
6. 專案結構: 請參見[專案結構](#🗂專案結構)
7. 編譯執行檔: 使用*PyInstaller*搭配`main.spec`進行打包
   ```
   pyinstaller main.spec
   ```


## **🛠使用技術**
- *Tkinter*: 撰寫GUI架構
- *yt-dlp*: 執行下載工作
- *多執行緒*: 使用多執行緒分配下載任務，避免視窗沒有回應
- *FFmpeg*: 負責轉檔工作，內置於`.exe`內


## **🗂專案結構**
```
musicDownloader/
├─ .gitignore
├─ ffmpeg_bin.zip      # ffmpeg/bin 之壓縮檔
├─ icon_v2.ico         # 執行檔圖示
├─ LICENSE
├─ main.py             # 主程式
├─ main.spec           # PyInstaller 打包設定檔
├─ README.md
└─ requirements.txt    # 開發環境所需套件
```


## **ℹ️備註**
- 維護者: 294Ryan - [Github](https://github.com/294Ryan)
- 使用條款: `MIT license`
- ⚠️本專案供教育研究使用，使用時請尊重所有版權與權利擁有者。
任何因不當使用造成的後果請自負。


---
# ***Music Downloader***

## **📜Table of Contents**
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Usage Guide](#usage-guide)
- [Development Notes](#development-notes)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Notes](#notes)


## **✏️Project Overview**
A Tkinter GUI application that downloads YouTube videos and automatically converts them into `.mp3` files.


## **✨Key Features**
- Clean and user-friendly **GUI** interface
- Automatically **trims URLs** to download only the current video's audio instead of the entire playlist
- Customizable download destination folder
- Downloads YouTube videos from a specified URL and **automatically converts** them into `.mp3` files
- Supports one-click **paste/clear** for the URL input field
- Displays a **progress bar** while downloading
- The `.exe` executable comes with a built-in **`ffmpeg` tool**, so no additional installation is required


## **✅️Usage Guide**
Please download the files from the Release section first.

- Launch: Run `musicDownloader_v2.4.exe`
- Feature Guide:

1. *Enter a YouTube Video URL:*

   Enter the URL into the `YouTube URL` input box, or click the `Paste` button on the right to paste directly from the clipboard.

2. *Select the Download Destination Folder:*

   The default save location is your computer's `Downloads` folder.

   Click the `Select` button on the right side of the window to choose a custom destination folder.

   Click the `Open Folder` button to automatically open the selected or default destination folder.

3. *Start Downloading:*

   Click the `Download Video` button to start a background thread that downloads the video and converts it into an `.mp3` file, saved to the selected or default destination folder.

   During the download process, messages such as *Preparing Download*, *Download Progress*, and *Download Complete* will appear in sequence.

   If the URL is invalid, a warning message box saying *Download Failed* will appear. Please follow the instructions and try again.


## **💻Development Notes**
1. Please read the Development Guidelines below.
2. Clone this repository to your local machine:
```
cd directory
git clone github.com/294Ryan/MusicDownloader.git
```

3. Programming Language:
   - Python 3.13

4. Install Required Tools:
   - Python modules: Run the following command
     ```
     pip install -r requirements.txt
     ```
   - FFmpeg:

     Download it from <https://share.google/977WgCDSa2UqLznsR>, or extract `ffmpeg_bin.zip` from this repository and place the resulting `ffmpeg_bin` folder in the project root.

5. Technologies Used: Please refer to [Technologies Used](#🛠technologies-used)
6. Project Structure: Please refer to [Project Structure](#🗂project-structure)
7. Compile executable file: Package with *PyInstaller* using `main.spec`
   ```
   pyinstaller main.spec
   ```


## **🛠Technologies Used**
- *Tkinter*: Used for building the GUI interface
- *yt-dlp*: Handles video downloading
- *Multithreading*: Prevents the window from freezing while downloading
- *FFmpeg*: Handles file conversion and is bundled inside the `.exe` executable


## **🗂Project Structure**
```
musicDownloader/
├─ .gitignore
├─ ffmpeg_bin.zip      # Compressed archive of ffmpeg/bin
├─ icon_v2.ico         # Executable icon
├─ LICENSE
├─ main.py             # Main program
├─ main.spec           # PyInstaller build configuration
├─ README.md
└─ requirements.txt    # Dependencies required for development
```


## **ℹ️Notes**
- Maintainer: 294Ryan - [GitHub](https://github.com/294Ryan)
- License: `MIT License`
- ⚠️ This project is intended for educational and research purposes only. Please respect all copyrights and rights holders when using this software.
Any consequences caused by improper use are the user's own responsibility.
