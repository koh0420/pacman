"""
プロジェクト内のパラメータを管理するためのモジュール．

A) プログラムを書くときにやること．
  1) デフォルトパラメータを `Parameters` クラス内で定義する．
  2) コマンドライン引数を `common_args` 内で定義する．

B) パラメータを指定して実行するときにやること．
  1) `python config.py` とすると，デフォルトパラメータが `parameters.json` というファイルに書き出される．
  2) パラメータを指定する際は，Parametersクラスを書き換えるのではなく，jsonファイル内の値を書き換えて，
  `python main.py -p parameters.json`
  のようにjsonファイルを指定する．
"""

from dataclasses import dataclass, field
from utils import dump_params
from argparse import ArgumentParser


@dataclass(frozen=True)
class Parameters:
    """
    プログラム全体を通して共通のパラメータを保持するクラス．
    ここにプロジェクト内で使うパラメータを一括管理する．
    """
    args: dict = field(default_factory=lambda: {})  # コマンドライン引数
    run_date: str = ''  # 実行時の時刻
    git_revision: str = ''  # 実行時のプログラムのGitのバージョン

    f_size: int = 30  # フィールドサイズ フィールドの1辺の長さ
    p_num: int = 1  # プレイヤーの数
    e_num: int = 5  # 敵の数
    f_num: int = 3  # 食べ物の数
    w_num: int = 20  # 壁の数


def common_args(parser: 'ArgumentParser'):
    """
    コマンドライン引数を定義する関数．
    Args:
        parser (:obj: ArgumentParser):
    """
    parser.add_argument(
        "-p",
        "--parameters",
        help="パラメータ設定ファイルのパスを指定．デフォルトはNone",
        type=str,
        default=None)
    # コマンドライン引数を指定
    return parser


if __name__ == "__main__":
    dump_params(Parameters(), './', partial=True)  # デフォルトパラメータを
