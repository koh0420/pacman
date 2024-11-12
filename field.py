from player import Player
from enemy import Enemy
from wall import Wall
from food import Food
import random
"""
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

    def __init__(self, p: int, e: int, w: int, f: int, size: int) -> None:
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
        self.f_size = size
        self.items: list[Player | Enemy | Wall | Food] = []
        self.create_field(size)
        for _ in range(p):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position
                    if item_pos == rand_pos:
                        can_set = False
                        break
                if can_set is True:
                    self.items += [Player(rand_pos[0], rand_pos[1])]
                    break
        for _ in range(e):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position
                    if item_pos == rand_pos:
                        can_set = False
                        break
                if can_set is True:
                    self.items += [Enemy(rand_pos[0], rand_pos[1])]
                    break
        for _ in range(w):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position
                    if item_pos == rand_pos:
                        can_set = False
                        break
                if can_set is True:
                    self.items += [Wall(rand_pos[0], rand_pos[1])]
                    break
        for _ in range(f):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position
                    if item_pos == rand_pos:
                        can_set = False
                        break
                if can_set is True:
                    self.items += [Food(rand_pos[0], rand_pos[1])]
                    break

    def display(self) -> None:
        """
        アイテムの表示を行う関数
        Args:
            None
        Returns:
            None
        Examples:
            >>> f = Field(1,1,0,0,4)
            >>> print(type(f.items[12]))
            <class 'player.Player'>
            >>> f.items[12].move((1,1))
            >>> print(type(f.items[13]))
            <class 'enemy.Enemy'>
            >>> f.items[13].move((2,1))
            >>> f.display()
            🧱🧱🧱🧱
            🧱👽🤡🧱
            🧱　　🧱
            🧱🧱🧱🧱
        """
        disp_list = [["　"] * self.f_size for i in range(self.f_size)]
        for item in self.items:
            item_x, item_y = item.get_now_position()
            disp_list[item_y][item_x] = item.icon
        for i in range(self.f_size):
            print("".join(disp_list[i]))

    def update(self) -> None:
        """
        敵の動きなどを更新する関数
        Args:
            None
        Returns:
            None
        Examples:
            pass
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
            🧱🧱🧱🧱
            🧱　　🧱
            🧱　　🧱
            🧱🧱🧱🧱
        """
        for i in range(self.f_size):
            for j in range(self.f_size):
                if i == 0 or i == self.f_size-1:
                    self.items += [Wall(i, j)]
                elif j == 0 or j == self.f_size-1:
                    self.items += [Wall(i, j)]

    def hit_check(self) -> list[int, list[int]]:
        """
        アイテムがどのアイテムと衝突したかをチェックする関数
        Args:
            None
        Returns:
            list[int,list[int]]:アイテムが衝突したアイテムのインデックスのリスト
        Examples:
            pass
        """
        """
        items_hit_list: list[Player | Enemy | Wall | Food] = []
        for item in self.items:
            item_hit_list: list[Player | Enemy | Wall | Food, list[Player | Enemy | Wall | Food]] = [item, []]
            for hit_item in self.items:
                if item != hit_item:
                    if item.get_next_position == hit_item.get_next_position:
                        item_hit_list[item] += [hit_item]
            items_hit_list += items_hit_list
        return items_hit_list
        """


if __name__ == "__main__":
    import doctest
    doctest.testmod()
