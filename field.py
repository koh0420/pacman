"""
from player import Player
"""


class Field:
    """Fieldクラス
    ゲームのフィールドの表示やItemを親に持つクラスの処理を行うクラス.
    Item同士の衝突判定,キーボード入力判定,プレイヤーと敵へ移動命令の機能を持つ.

    Attributes:
        self.items (list[Enemy|Player]):アイテムのリスト
        self.field (list[list[str]]):表示するためのフィールドの情報
        self.f_size (int):フィールドのサイズ
    """

    def __init__(self) -> None:
        """
        Fieldの初期化を行う関数
        Args:
            p (int):プレイヤーの数
            e (int):敵の数
            w (int):壁(障害物)の数
            f (int):食べ物の数
            size (int):フィールドのサイズ
        Returns:
            None
        """
        pass

    def display(self) -> None:
        """
        アイテムの表示を行う関数
        Args:
            None
        Returns:
            None
        Examples:
            >>> f = Field(1,1,0,1,4)
            >>> f.display()
            WWWW
            WPEW
            WF W
            WWWW
        """
        pass

    def update(self) -> None:
        """
        敵の動きなどを更新する関数
        Args:
            None
        Returns:
            None
        """
        pass

    def create_field(self, f_size) -> None:
        """
        フィールドに壁を設置する関数
        Args:
            f_size (int):フィールドのサイズ
        Returns:
            None
        Examples:
            >>> f = Field(0,0,0,0,4)
            >>> f.display()
            WWWW
            W  W
            W  W
            WWWW
        """
        pass

    def hit_check(self) -> list[int, list[int]]:
        """
        アイテムがどのアイテムと衝突したかをチェックする関数
        Args:
            None
        Returns:
            list[int,list[int]]:アイテムが衝突したアイテムのインデックスのリスト
        Examples:
            >>> f = Field(1,1,0,0,4)
            >>> print(type(f.field[0]) is Player)
            True
            >>> f.field[0].now_x = 1
            >>> f.field[0].now_y = 1
            >>> f.field[0].next_x = 1
            >>> f.field[0].next_y = 2
            >>> print(type(f.field[0]) is Enemy)
            False
            >>> f.field[1].now_x = 2
            >>> f.field[1].now_y = 2
            >>> f.field[1].next_x = 1
            >>> f.field[1].next_y = 2
            >>> printf(f.hit_check())
            [0,[1]]
            >>> f.field[1].next_x = 2
            >>> f.field[1].next_y = 1
            >>> printf(f.hit_check())
            [0,[]]
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
