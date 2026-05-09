# 🎵 MusicDownloader v2.3

A lightweight, Python-based YouTube-to-MP3 downloader featuring a clean Graphical User Interface (GUI). This tool allows users to convert YouTube videos into high-quality audio files with real-time progress tracking and a seamless user experience.

---

## ✨ Key Features

### 1. Smart URL Handling (v1.1+)
*   **Single File Enforcement**: Automatically detects and trims `&list=...` parameters from URLs. This ensures only the specific video you want is downloaded, preventing the app from accidentally downloading entire playlists.

### 2. Enhanced User Experience (v2.3)
*   **Visual Progress Bar**: Real-time percentage display and progress bar keep you informed of the download status.
*   **Quick Action Buttons**: Includes dedicated **"Paste"** and **"Clear"** buttons to streamline the workflow without manual typing.
*   **Directory Management**: Easily customize the save location and use the **"Open Folder"** shortcut to access your files instantly.

### 3. Technical Optimizations (v2.3)
*   **Multi-Threading**: Uses Python’s `threading` module to run downloads in the background, ensuring the GUI remains responsive and never shows a "Not Responding" status.
*   **Portable Design**: 
    *   Compatible with `PyInstaller` for easy packaging.
    *   Supports a local `ffmpeg_bin` directory within the application folder, eliminating the need to set up system environment variables.
*   **Timestamp Correction**: Automatically updates the file's "Last Modified" time upon completion, making it easier to find your newest downloads when sorting by date.

---

## 🛠️ Tech Stack

*   **Language**: Python 3.x
*   **Core Libraries**:
    *   `yt-dlp`: A powerful engine for media extraction.
    *   `Tkinter`: Python’s standard toolkit for the Graphical User Interface.
*   **Dependencies**: `FFmpeg` (Required for high-quality MP3 conversion).

---

## 🚀 Getting Started

### Prerequisites
1. Ensure Python 3.x is installed on your system.
2. Install the required Python package:
   ```
   pip install yt-dlp
   ```
   

4. **FFmpeg Setup**:
Place your `ffmpeg` binaries inside a folder named `ffmpeg_bin` in the project root directory. The app is pre-configured to look for `ffmpeg` in this specific path for maximum portability.

### Running the Application

Execute the script using the following command:
```
python MusicDownloader.py
```

---

## 📖 How to Use

1. **Copy URL**: Copy a YouTube video link from your browser.
2. **Paste**: Click the **[貼上Paste]** button in the application.
3. **Select Path**: The default save location is your system "Downloads" folder. Click **[選擇Select]** to change it if desired.
4. **Download**: Click **[下載影片Download Video]**.
5. **Finish**: Once the progress bar reaches 100%, click **[開啟資料夾Open Folder]** to view your MP3.

---

## 📋 Changelog

* **v1.1**: Added URL index filtering to solve the "entire playlist download" issue.
* **v2.3**:
* Major UI overhaul with added Progress Bar and Status Messages.
* Implemented Threading to fix GUI freezing during downloads.
* Optimized `ffmpeg` path logic for better portability across different computers.



---

## ⚠️ Disclaimer

This tool is intended for personal use and educational purposes only. Please respect the copyrights of content creators. Do not use this software for commercial purposes or for the illegal distribution of copyrighted material.
