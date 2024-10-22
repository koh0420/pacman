class Item:
    """block,player,enemy,foodの親クラス

    Attributes:
       now_x(int) : 現在のx座標
       now_y(int) : 現在のy座標
       next_x(int) : 次の時刻でのx座標
       next_y(int) : 次の時刻でのy座標
       status(bool) : アイテムの状態（Trueなら存在する、Falseなら存在しない消滅した）
       icon(str) : 表示されるアイテムのアイコン
    """
    def __init__(self, x, y) -> None:
        """
        Itemクラスのコンストラクタ
        引数にx座標とy座標を受け取り、それぞれの座標を初期化する

        Args:
            x(int): x座標
            y(int): y座標

        Returns:
            None

        Examples:
            item = Item(4, 5)
            item.now_x -> 4
            item.now_y -> 5
            item.next_x -> 4
            item.next_y -> 5
            item.icon -> ''
            item.status -> True
        """
        pass

    def get_now_position(self) -> tuple[int, int]:
        """
        現在の座標を返す.

        Returns:
            tuple[int,int]:現在の座標

        Example
            >>> item = Item(1,2)
            >>> item.get_now_position()
            (1,2)
        """
        pass

    def move(self, move_to: tuple[int, int]) -> None:
        """
        受け取った移動先の座標に今の座標を変換して移動する
        Args:
            move_to(tuple[int,int]):移動先の座標

        Returns:
            None

        Example
            >>> item = Item(1,2)
            >>> item.get_now_position()
            (1,2)
            >>> item.move(3,2)
            >>> item.get_now_position()
            (3,2)
        """
        pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
