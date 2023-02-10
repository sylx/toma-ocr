import sys
import os
import cv2
import pyocr
from PIL import Image, ImageEnhance


def resourcePath(filename):
  if hasattr(sys, "_MEIPASS"):
      return os.path.join(sys._MEIPASS, filename)
  return os.path.join(filename)

def run_script(filepath):
    f=open(filepath, 'r', encoding='utf-8')
    os.environ["PATH"] += os.pathsep + os.path.abspath(resourcePath("tesseract-bin"))
    os.environ["TESSDATA_PREFIX"] = os.path.abspath(resourcePath("data/tessdata"))
    exec(f.read(),{
        '__file__':os.path.abspath(filepath),
        'resoucePath':resourcePath
    })


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        filepath = 'ocr.py'
    run_script(filepath)
