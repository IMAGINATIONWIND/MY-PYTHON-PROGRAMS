import win32gui
import win32con
import win32api
from pytube import YouTube
import threading


WINDOW_CLASS = "YTDownloaderWin32"
FONT = None

# Show message in output box
def set_output(text):
    win32gui.SendMessage(output_box, win32con.WM_SETTEXT, 0, text)

# Download video (
def download_video(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        set_output(f"Downloading: {yt.title}\nQuality: {stream.resolution}")
        stream.download()
        set_output("Download complete!")
    except Exception as e:
        set_output(f"Error: {e}")

# Download audio (threaded)
def download_audio(url):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        set_output(f"Downloading Audio: {yt.title}")
        stream.download(filename=f"{yt.title}.mp3")
        set_output("Audio Download complete!")
    except Exception as e:
        set_output(f"Error: {e}")

# qualities

def list_qualities(url):
    try:
        yt = YouTube(url)
        qualities = "\n".join([s.resolution for s in yt.streams.filter(progressive=True)])
        set_output("Available Qualities:\n" + qualities)
    except Exception as e:
        set_output(f"Error: {e}")
        
# Win32 Window Procedure

def window_proc(hwnd, msg, wparam, lparam):
    if msg == win32con.WM_COMMAND:
        control_id = win32api.LOWORD(wparam)

        if control_id == 1:  # List qualities
            url = win32gui.GetWindowText(url_box)
            threading.Thread(target=list_qualities, args=(url,), daemon=True).start()

        elif control_id == 2:  # Download video
            url = win32gui.GetWindowText(url_box)
            threading.Thread(target=download_video, args=(url,), daemon=True).start()

        elif control_id == 3:  # Download audio
            url = win32gui.GetWindowText(url_box)
            threading.Thread(target=download_audio, args=(url,), daemon=True).start()

    elif msg == win32con.WM_DESTROY:
        win32gui.PostQuitMessage(0)

    return win32gui.DefWindowProc(hwnd, msg, wparam, lparam)

# GUI

wc = win32gui.WNDCLASS()
wc.lpfnWndProc = window_proc
wc.lpszClassName = WINDOW_CLASS
win32gui.RegisterClass(wc)

hwnd = win32gui.CreateWindow(
    WINDOW_CLASS,
    "YouTube Downloader (Win32 GUI)",
    win32con.WS_OVERLAPPEDWINDOW,
    200, 200, 500, 300,
    0, 0, 0, None
)

url_box = win32gui.CreateWindow(
    "EDIT", "",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.WS_BORDER,
    20, 20, 440, 25,
    hwnd, 1000, 0, None
)

# Buttons
btn_list = win32gui.CreateWindow(
    "BUTTON", "List Qualities",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    20, 60, 130, 30,
    hwnd, 1, 0, None
)

btn_video = win32gui.CreateWindow(
    "BUTTON", "Download Video",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    170, 60, 130, 30,
    hwnd, 2, 0, None
)

btn_audio = win32gui.CreateWindow(
    "BUTTON", "Download Audio",
    win32con.WS_CHILD | win32con.WS_VISIBLE,
    320, 60, 130, 30,
    hwnd, 3, 0, None
)

output_box = win32gui.CreateWindow(
    "EDIT", "",
    win32con.WS_CHILD | win32con.WS_VISIBLE | win32con.ES_MULTILINE |
    win32con.WS_VSCROLL | win32con.ES_AUTOVSCROLL | win32con.ES_READONLY | win32con.WS_BORDER,
    20, 110, 440, 130,
    hwnd, 4, 0, None
)

win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
win32gui.UpdateWindow(hwnd)

win32gui.PumpMessages()
