# Pacman Project

2024年度問題解決型プログラミンググループ課題(Pacmanもどき)

## Requirement
- Python 3.12.5


## Installation
- 結果出力用ディレクトリを作成
```shell
mkdir result
```
- 各種モジュールのインストール
```shell
pip install -r requirements.txt
```


## Usage
- メインプログラムを実行．
  - キーボード入力(W:↑,A:←,S:↓,D:→)に応じてPlayerを操作できる.
  - `result/[日付][実行時刻]/` 下に実行結果とログが出力されます．
```shell
python main.py
```
- パラメータ変更方法
  - デフォルトのパラメータ設定をjson出力．
```shell
python config.py  # parameters.jsonというファイルが出力される．
```
  - 以下のように，上記で生成されるjsonファイルの数値を書き換えて，実行時のパラメータを指定できます．
```shell
python main.py -p parameters.json
```



## Parameter Settings

- 指定できるパラメータは以下の通り．
```json
{
    "f_size": 20, #フィールドの大きさ
    "p_num": 1, #プレイヤーの数
    "e_num": 3, #敵の数
    "f_num": 4, #食べ物の数
    "w_num": 3, #壁の枚数
}
```

## Directory Structure
- プロジェクトの構成は以下の通り．
```shell
.
├── config.py           # パラメータ定義
├── main.py             # 実行ファイル
├── game.py             # Gameクラス
├── input_without_enter.py             # キーボード入力を受け取るクラス
├── input.py             # 特定の入力に対して処理を実行するクラス
├── field.py             # Fieldクラス
├── item.py             # Player,Enemy,Food,Wallの親クラス
├── player.py             # Playerクラス
├── enemy.py             # Enemyクラス
├── food.py             # Foodクラス
├── wall.py             # Wallクラス
├── parameters.json     # パラメータ指定用ファイル
├── result              # 結果出力ディレクトリ
│   └── 20211026_165841
└── utils.py            # 共有関数群
```
