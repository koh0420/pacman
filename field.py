from player import Player
"""

"""
class Field:
    """Fieldクラス
    ゲームのフィールドの表示やItemを親に持つクラスの処理を行うクラス.
    Item同士の衝突判定,キーボード入力判定,プレイヤーと敵へ移動命令の機能を持つ.

    Attributes:
        self.items (list[Food|Wall|Enemy|Player]):アイテムのリスト
        self.field (list[list[str]]):表示するためのフィールドの情報
        self.f_size (int):フィールドのサイズ
    """

    def __init__(self) -> None:
        """
        Fieldの初期化を行う関数
        
        Args:
            number_of_players (int):プレイヤーの数
            number_of_enemys (int):敵の数
            number_of_walls (int):壁(障害物)の数
            number_of_foods (int):食べ物の数
            f_size (int):フィールドのサイズ
        """
        pass
    
    pass