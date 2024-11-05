"""プレイヤー(パックマン)にcontrolから入力方向を受け取ってItemから受け継いだ座標と移動メソッドを用いて移動する"""
from item import Item


class Player(Item):
    """プレイヤークラス
    Itemを継承して作成したプレイヤークラス.
    入力から移動方向を受け取って移動しようとする方向を計算するメソッドと
    マップから移動して良いと許可が出た時に呼び出される座標を更新するメソッド
    を追加.

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
    """
    def __init__(self, x, y) -> None:
        """x,yを初期化し、プレイヤー(パックマン)の見た目を設定"""
        super().__init__(x, y)
        self.icon = "👽"

    def get_next_position(self, direction: int) -> tuple[int, int]:
        """移動後の座標を返す
        Args:
            direction(int):行きたい方向

        Returns:
            tuple[int, int]:移動先の座標([x座標,y座標])

        Example:
            >>> player = Player(1,2)
            >>> player.get_next_position(0)
            (1, 1)
            >>> player = Player(1,2)
            >>> player.get_next_position(1)
            (2, 2)
            >>> player = Player(1,2)
            >>> player.get_next_position(2)
            (1, 3)
            >>> player = Player(1,2)
            >>> player.get_next_position(3)
            (0, 2)
        """
        if (direction == 0):
            self.next_x = self.now_y - 1
        elif (direction == 1):
            self.next_y = self.now_x + 1
        elif (direction == 2):
            self.next_x = self.now_y + 1
        elif (direction == 3):
            self.next_y = self.now_x - 1

        return (self.next_x, self.next_y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
