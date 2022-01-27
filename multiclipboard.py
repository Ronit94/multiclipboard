from pathlib import Path
from pprint import pprint
import clipboard


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
                    fb.write(clipboard.paste() + '\n')
                    self.old = clipboard.paste()
                    fb.close()
        except FileNotFoundError as Error:
            pprint(Error)


if __name__ == "__main__":
    clip_obj = MultiClipBoard()
    clip_obj.TrackClipBoard()
