from pathlib import Path
from pprint import pprint
import clipboard
from datetime import datetime
import time


class MultiClipBoard:
    def __init__(self):
        self.file = Path('multidata.txt')
        self.file.touch(exist_ok=True)
        self.old = None

    def TrackClipBoard(self):
        print("======================Clipboard tracking started=========================")
        try:
            while True:
                if self.old != clipboard.paste():
                    fb = open(self.file, 'a')
                    fb.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + ":->" + clipboard.paste() + '\n')
                    self.old = clipboard.paste()
                    fb.close()
                    time.sleep(0.5)
        except FileNotFoundError as Error:
            pprint(Error)


if __name__ == "__main__":
    clip_obj = MultiClipBoard()
    clip_obj.TrackClipBoard()
