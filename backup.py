from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import shutil
import time


class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(DOWNLOADS):
            if filename.endswith(".docx") or filename.endswith(".pdf") or filename.endswith(".csv") or filename.endswith(".txt"):
                fileD = DOWNLOADS + "/" + filename
                newD = DOCUMENTS + "/" + filename
                os.rename(fileD, newD)
                print(f"Moved {filename} to {DOCUMENTS}")
            elif filename.endswith(".mp3") or filename.endswith(".wav"):
                fileM = DOWNLOADS + "/" + filename
                newM = MUSIC + "/" + filename
                os.rename(fileM, newM)
                print(f"Moved {filename} to {MUSIC}")
            elif filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(
                    ".avi") or filename.endswith(".amv"):
                fileV = DOWNLOADS + "/" + filename
                newV = VIDEO + "/" + filename
                os.rename(fileV, newV)
                print(f"Moved {filename} to {VIDEO}")
            elif filename.endswith(".png") or filename.endswith(".jpg"):
                fileI = DOWNLOADS + "/" + filename
                newI = IMGS + "/" + filename
                os.rename(fileI, newI)
                print(f"Moved {filename} to {IMGS}")
            elif filename.endswith(".exe"):
                fileE = DOWNLOADS + "/" + filename
                newE = EXE + "/" + filename
                os.rename(fileE, newE)
                print(f"Moved {filename} to {EXE}")
            elif filename.endswith(".rar") or filename.endswith(".zip"):
                fileR = DOWNLOADS + "/" + filename
                newR = RAR + "/" + filename
                os.rename(fileR, newR) 
                print(f"Moved {filename} to {RAR}")


DOWNLOADS = "c:/users/guydo/downloads"
DOCUMENTS = "c:/users/guydo/documents"
MUSIC = "c:/users/guydo/music"
VIDEO = "c:/users/guydo/video"
IMGS = "c:/users/guydo/pictures"
EXE = "c:/users/guydo/exe"
RAR = "c:/users/guydo/rar"
event_handler = myHandler()
observer = Observer()
observer.schedule(event_handler, DOWNLOADS, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    print("stopped")
observer.join()
