from item import Item


class Wall(Item):
    """プレイヤークラス
    Itemを継承して作成した壁クラス.
    壁の見た目を設定する

    Attributes:
        self.icon(str) : 表示されるアイテムのアイコン
        self.now_x(int) : 現在のx座標
        self.now_y(int) : 現在のy座標
    """
    def __init__(self, x, y) -> None:
        """x,yを初期化し、壁の見た目を設定"""
        super().__init__(x, y)
        self.icon = "🧱"
