from item import Item
import random


class Enemy(Item):
    """エネミークラス
    Itemを継承して作成したクラスでランダムな方向を受け取り、移動仕様とするメソッドと
    マップから移動して良いと許可が出たら座標を更新するメソッド

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
        self.next_x(int) : 次の時刻でのx座標
        self.next_y(int) : 次の時刻でのy座標
        self.status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した
    """
    def __init__(self, x, y) -> None:
        """x,yを初期化し、enemyの見た目を設定"""
        super().__init__(x, y)
        self.icon = "🤡"

    def get_next_position(self) -> tuple[int, int]:
        """ランダムな方向に対して移動後の座標を計算して返す

        Returns:
            tuple[int, int]:移動先の座標([x座標,y座標])

        Example:
            >>> enemy = Enemy(1,2)
            >>> possible_moves = [(2, 2), (0, 2), (1, 3), (1, 1)]
            >>> next_move = enemy.get_next_position()
            >>> next_move in possible_moves
            True
        """
        rand_direction = random.randrange(4)

        if (rand_direction == 0):
            self.next_x = self.now_x + 1
        elif (rand_direction == 1):
            self.next_y = self.now_y + 1
        elif (rand_direction == 2):
            self.next_x = self.now_x - 1
        elif (rand_direction == 3):
            self.next_y = self.now_y - 1
        return (self.next_x, self.next_y)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
