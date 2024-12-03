from player import Player
from enemy import Enemy
from wall import Wall
from food import Food
import random
import math
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

    def __init__(self, p: int, e: int, f: int, w: int, size: int) -> None:
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
        self.create_field(w)
        for _ in range(p):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position()
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
                    item_pos = item.get_now_position()
                    if item_pos == rand_pos:
                        can_set = False
                        break
                if can_set is True:
                    self.items += [Enemy(rand_pos[0], rand_pos[1])]
                    break
        for _ in range(f):
            while len(self.items) < size**2:
                rand_pos = (random.randrange(size), random.randrange(size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position()
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
        hit_list = self._hit_check()
        after_items = self.items
        delete_list = []
        for hit in hit_list:
            item = after_items[hit[0]]
            for hit_items in hit[1]:
                hit_item = after_items[hit_items]
                if type(hit_item) is Wall:
                    item_index = self.items.index(item)
                    after_items[item_index].next_x = after_items[item_index].now_x
                    after_items[item_index].next_y = after_items[item_index].now_y
                if type(hit_item) is Food:
                    if type(item) is Enemy:
                        item_index = self.items.index(item)
                        after_items[item_index].next_x = after_items[item_index].now_x
                        after_items[item_index].next_y = after_items[item_index].now_y
                    elif type(item) is Player:
                        delete_list += [after_items.index(hit_item)]
                if type(hit_item) is Enemy:
                    if type(item) is Enemy:
                        item_index = self.items.index(item)
                        after_items[item_index].next_x = after_items[item_index].now_x
                        after_items[item_index].next_y = after_items[item_index].now_y
                    elif type(item) is Player:
                        delete_list += [after_items.index(item)]
                if type(hit_item) is Player:
                    if type(item) is Player:
                        item_index = self.items.index(item)
                        after_items[item_index].next_x = after_items[item_index].now_x
                        after_items[item_index].next_y = after_items[item_index].now_y

        self.item = after_items
        for item in self.items:
            if isinstance(item, (Player, Enemy)):
                item.move((item.next_x, item.next_y))
            if after_items.index(item) in delete_list:
                
                del self.items[after_items.index(item)]

    def create_field(self, wall_num) -> None:
        """
        フィールドに壁を設置する関数
        Args:
            wall_num (int):追加する壁の数
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
        
        for _ in range(wall_num):
            while len(self.items) < self.f_size**2:
                candiate_pos = (random.randrange(self.f_size), random.randrange(self.f_size))
                can_set = True
                for item in self.items:
                    item_pos = item.get_now_position()
                    if item_pos == candiate_pos:
                        can_set = False
                        break
                if can_set is True:
                    nearest_wall = []
                    for item in self.items:
                        if type(item) is Wall:
                            distance = math.sqrt((item.now_x - candiate_pos[0])**2 + (item.now_y - candiate_pos[1])**2)
                            nearest_wall += [[item, distance]]
                    min_distance = min(nearest_wall, key=lambda x: x[1])[1]
                    nearest_wall = [item for item in nearest_wall if item[1] == min_distance]

                    print(nearest_wall)
                    set_pos = [nearest_wall[0][0].now_x, nearest_wall[0][0].now_y]
                    set_dir_x = 0
                    set_dir_y = 0
                    if set_pos[0] > candiate_pos[0]:
                        set_dir_x = -1
                    elif set_pos[0] < candiate_pos[0]:
                        set_dir_x = 1
                    if set_pos[1] > candiate_pos[1]:
                        set_dir_y = -1
                    elif set_pos[1] < candiate_pos[1]:
                        set_dir_y = 1
                    
                    print("target:",candiate_pos)
                    for __ in range(int(nearest_wall[0][1])):
                        set_pos[0] += set_dir_x
                        set_pos[1] += set_dir_y
                        print(set_pos)
                        self.items += [Wall(set_pos[0], set_pos[1])]
                    break

    def _hit_check(self) -> list[int, list[int]]:
        """
        アイテムがどのアイテムと衝突したかをチェックする関数
        Args:
            None
        Returns:
            list[int,list[int]]:アイテムが衝突したアイテムのインデックスのリスト
        Examples:
            pass
        """
        items_hit_list = []
        for item in self.items:
            hit_list = []
            for hit_item in self.items:
                if item != hit_item:
                    if isinstance(item, (Player, Enemy)):
                        item_next_pos = (item.next_x, item.next_y)
                        item_now_pos = item.get_now_position()
                        hit_now_pos = hit_item.get_now_position()
                        if isinstance(hit_item, (Food, Wall)):
                            if item_next_pos == hit_now_pos:
                                hit_list += [self.items.index(hit_item)]
                        if isinstance(hit_item, (Player, Enemy)):
                            hit_next_pos = (hit_item.next_x, hit_item.next_y)
                            if item_next_pos == hit_next_pos:
                                hit_list += [self.items.index(hit_item)]
                            if (item_next_pos == hit_now_pos) and (item_now_pos == hit_next_pos):
                                hit_list += [self.items.index(hit_item)]
            if hit_list != []:
                items_hit_list += [[self.items.index(item), hit_list]]
        return items_hit_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()
