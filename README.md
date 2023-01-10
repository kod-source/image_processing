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
python3に対応させた別バージョンは下記のコマンドでインストールする
```
pip install "ocrd-fork-pylsd == 0.0.3"
```
※既に `pip install pylsd` でpylsdをインストールしてしまっていると名前衝突が起きてしまうことがあるので削除を推奨します。
上記のコマンドを実行してもPylsdがインストールされていないエラーが出るケースが稀にある
そのような時は、既にインストールしているPylsdを削除して下記のフォーク版を試す
```
pip install pylsd-nova
```
* Apple SiliconのMacを使用している場合はARM版をインストールすること
```
pip install pylsd-nova-mac-arm
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
```
python script/click_script.py
```

