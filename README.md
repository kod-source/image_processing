# 画像処理　倍率自動測定
画像処理の倍率自動測定です。<br />
pythonを使用し、画像を読み取りその画像を倍率を自動で測定するプログラムです。

## 必要なツール
- python
- open cv
- Pylsd

### pythonのインストール方法
[こちらのリンク](https://www.python.org/downloads/)から各OSに沿ったインストーラーをダウンロードしてパッケージを実行してください。
- pythonがインストールされているか確認する
```
python --version
```
pythonがインストールされていれば、pythonのバージョンを確認することができます。

### open cv インストール方法
下記のコマンドを実行してインストールする
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
- 上記のコマンドでPylsdをインストールしてもPylsdがインストールされていないエラーが出るケースが稀にあるので、そのような時は既にインストールしているPylsdを削除して下記のフォーク版を試す
```
pip install pylsd-nova
```
- Apple SiliconのMacを使用している場合はARM版をインストールすること
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

## 実行手順
1. imgフォルダー内に倍率を測定したい画像を配置する
1. `script/click_script.py`の4行目の`file_name`の変数値を①のファイル名に変更する（今後実行する際に引数でファイル名を指定するように修正予定）
1. scriptフォルダー配下にあるファイルを指定して実行する
    1. 下記のコマンドでpythonを実行する（ファイル名は適宜合わせること）
    ```
    python script/click_script.py
    ```
1. 下記のように線文が検出された画像であるか確認する
    <br /><img width="300" height="300" alt="image" src="https://user-images.githubusercontent.com/74532799/211551926-929b27d6-c826-45c7-a8bf-9de8e2a93066.png">
1. 距離を求めたい2点をクリックする
    1. 2点をクリックすると下記のように倍率と誤差率を表示している
    1. `result`には倍率の測定結果、`diff`には誤差率を表示している（今後日本語の表示にも対応する予定） 
    <br /><img width="300" height="300" alt="image" src="https://user-images.githubusercontent.com/74532799/211552984-7b830723-f954-4494-89f6-2e5f1294c58a.png">




