import sys
#ライブラリのインポート
import cv2
#画像のパス
path = 'popo.jpg'
i = cv2.imread(path, 0)

#閾値、最大輝度値、二値化処理
th = 127
i_max = 255
ret, i_binary = cv2.threshold(i, th, i_max, cv2.THRESH_BINARY)

#出力画像のパスと画像保存
path_o = 'popo_binary.jpg'
cv2.imwrite(path_o, i_binary)

#ライブラリのインポート
import pyocr
from PIL import Image, ImageEnhance
import os

#OCRエンジン取得
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

#OCRの設定
builder = pyocr.builders.TextBuilder(tesseract_layout=5)

#画像読み込み
img = Image.open('popo_binary.jpg')


#img_g = img.convert('L') #Gray変換
#enhancer= ImageEnhance.Contrast(img_g)
#img_con = enhancer.enhance(2.0)

#img=img.convert('RGB')
#size=img.size
#img2=Image.new('RGB',size)
 
#border=110
 
#for x in range(size[0]):
#    for y in range(size[1]):
#        r,g,b=img.getpixel((x,y))
#        if r > border or g > border or b > border:
#            r = 0
#            g = 255
#            b = 255
#        img2.putpixel((x,y),(r,g,b))
        
        

#画像からOCRで日本語を読んで、文字列として取り出す
txt_pyocr = tool.image_to_string(img , lang='jpn_vert', builder=builder)

#半角スペースを消す
txt_pyocr = txt_pyocr.replace(' ', '')

print(txt_pyocr)

#止める
input("ok?")