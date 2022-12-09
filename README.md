# 画像処理　倍率自動測定
画像処理の倍率自動測定です。<br />
pythonを使用し、画像を読み取りその画像を倍率を自動で測定するプログラムです。

## 必要なツール
- python
- open cv
- Pylsd

### open cv インストール方法
```
pip install opencv-python
pip install opencv-contrib-python
```
### Pylsd インストール方法
```
pip install pylsd
```
↑はpython3に対応していないので、
python3の方は対応させた別バージョン
```
pip install "ocrd-fork-pylsd == 0.0.3"
```

## ディレクトリ構成
```
.
├── img (元画像データを保管場所)
├── result (実行結果画像を保管する場所 (gitの配下には基本入れない))
└── script (pythonのスクリプト群)
```

## 実行方法
- scriptフォルダー配下にあるファイルを指定する
- 第1引数にファイル名を指定する
- 第2引数に倍率の真値を指定する （真値がわからない時は指定しなくても良い）
```
python script/click_script.py 10k.jpg 10000
```


