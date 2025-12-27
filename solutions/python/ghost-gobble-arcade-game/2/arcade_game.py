"""Functions for implementing the rules of the classic arcade game Pac-Man."""


def eat_ghost(power_pellet_active, touching_ghost):
    return power_pellet_active and touching_ghost

    """
    如果能量丸啟動 且 吃豆人能吃掉鬼魂 回傳 True
    (If the power pellet is activated and Pac‑Man can eat the ghosts, return True.)
    """


def score(touching_power_pellet, touching_dot):
    return touching_dot or touching_power_pellet

    """
    如果吃豆人正在碰觸能量丸，或碰觸小點，回傳 得分。
    (If Pac‑Man is touching a power pellet or touch a dot, return score.)
    """


def lose(power_pellet_active, touching_ghost):
    return(not power_pellet_active) and touching_ghost
    
    """
    如果吃豆人觸碰鬼魂且沒有啟動能量丸，回傳 輸
    (If Pac‑Man touches a ghost and has not activated a power pellet, return lose.)
    """
def win(has_eat_all_dot, power_pellet_active, touching_ghost):
    return has_eat_all_dot and not ( touching_ghost and (not power_pellet_active))
            
    """吃豆人吃光所有點 吃豆人有能力(彈丸啟動) 吃豆人沒有碰到鬼魂 回傳 贏
    (If Pac‑Man eats all the dots, Pac‑Man has the ability (power pellet activated), and Pac‑Man has not touched         any ghosts, return win.)
    """