EXPECTED_BAKE_TIME = 40  # 預期烘焙時間（分鐘）
PREPARATION_TIME = 40    # 預期準備時間（分鐘）

def bake_time_remaining(elapsed_bake_time):
    """
    備註: 計算剩餘烘焙時間。

    :param elapsed_bake_time: int - 已經過的烘焙時間（分鐘）
    :return: int - 剩餘烘焙時間（分鐘）
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    備註: 計算準備時間。

    :param number_of_layers: int - 千層麵層數
    :return: int - 準備時間（分鐘）
    """
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    備註: 計算總共已經花費的時間。

    :param number_of_layers: int - 千層麵層數
    :param elapsed_bake_time: int - 已經過的烘焙時間（分鐘）
    :return: int - 總共花費的時間（分鐘）
    """
    return elapsed_bake_time + preparation_time_in_minutes(number_of_layers)


# 範例呼叫
print(elapsed_time_in_minutes(3, 6))