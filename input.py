from input_without_enter import InputWithoutEnter


class UserInput:
    """ユーザーの入力を受け取るクラス"""

    @staticmethod
    def get_user_input(self) -> int:
        """ユーザの入力を受けとり、数字として方向を返す
        Returns:
            direction: ユーザーの入力した方向(1: ↑,2: →, 3: ↓,4: ←)
        """
        # キー入力を受け取る
        key = InputWithoutEnter.input_without_enter()
        # 入力されたキーに対応する方向を返す
        if key == "w":
            return 1
        elif key == "a":
            return 4
        elif key == "s":
            return 3
        elif key == "d":
            return 2
        else:
            return 0
