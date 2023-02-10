# toma-ocr

トーマのためのOCRをするpythonを実行ファイルにする全て

## conda

anaconda以外は、がんばれ

```bash
conda create --name toma --file conda_requirements.txt
conda activate toma
```

## tessaract-bin

https://github.com/UB-Mannheim/tesseract/wiki

にあるWindows版のインストーラーでインストールしたら

  C:\Program Files\Tesseract-OCR

にあるファイルを全部

tessaract-bin/にぶち込む（ディレクトリはぶち込まない）

## 他に使うモジュールがあればmain.pyで読み込んでおく

```python

# ocr.pyで使いたい外部パッケージ
import hogehoge
```

pyinstallerに組み込むモジュールはそういう感じでやる（すんなり出来るやつとそうでないやつがある。がんばれ

## exe作成

```bash
pyinstaller ocr.spec
```

成功すると
dist/ocr.exe

が出来ている。良かったな
