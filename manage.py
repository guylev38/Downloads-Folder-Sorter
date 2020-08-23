from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

import os
import shutil
import time

print("Press CTRL+C to stop the program")
class myHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(DOWNLOADS):
            if filename.endswith(".docx") or filename.endswith(".pdf") or filename.endswith(".csv") or filename.endswith(".txt") or filename.endswith(".doc"):
                fileD = DOWNLOADS + "/" + filename
                newD = DOCUMENTS + "/" + filename
                os.rename(fileD, newD)
                print(f"Moved {filename} to {DOCUMENTS}")
            elif filename.endswith(".mp3") or filename.endswith(".wav"):
                fileM = DOWNLOADS + "/" + filename
                newM = MUSIC + "/" + filename
                os.rename(fileM, newM)
                print(f"Moved {filename} to {MUSIC}")
            elif filename.endswith(".mp4") or filename.endswith(".mkv") or filename.endswith(".avi") or filename.endswith(".amv"):
                fileV = DOWNLOADS + "/" + filename
                newV = VIDEO + "/" + filename
                os.rename(fileV, newV)
                print(f"Moved {filename} to {VIDEO}")
            elif filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
                fileI = DOWNLOADS + "/" + filename
                newI = IMGS + "/" + filename
                os.rename(fileI, newI)
                print(f"Moved {filename} to {IMGS}")
            elif filename.endswith(".exe"):
                fileE = DOWNLOADS + "/" + filename
                newE = EXE + "/" + filename
                os.rename(fileE, newE)
                print(f"Moved {filename} to {EXE}")
            elif filename.endswith(".rar") or filename.endswith(".zip") or filename.endswith(".7z") or filename.endswith(".torrent"):
                fileR = DOWNLOADS + "/" + filename
                newR = RAR + "/" + filename
                os.rename(fileR, newR) 
                print(f"Moved {filename} to {RAR}")
            else:
                fileO = DOWNLOADS + "/" + filename
                newO = OTHER + "/" + filename
                os.rename(fileO, newO)
                print(f"Moved {filename} to {OTHER}")
DOWNLOADS = "c:/users/mayoto/downloads"
DOCUMENTS = "c:/users/mayoto/documents"
MUSIC = "c:/users/mayoto/music"
VIDEO = "c:/users/mayoto/videos"
IMGS = "c:/users/mayoto/pictures"
EXE = "c:/users/mayoto/exe"
RAR = "c:/users/mayoto/rar"
OTHER = "c:/users/mayoto/other"
event_handler = myHandler()
observer = Observer()
observer.schedule(event_handler, DOWNLOADS, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
    print("Program Terminated")
observer.join()
