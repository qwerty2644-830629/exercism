def value_of_card(card): # 計算牌的價值
    # card(牌的數字)
    pip = 0 # (點數)

    if card == "A": # A = 1
        pip = 1
    elif card == "J" or card == "Q" or card == "K": # J Q K  10
        pip = 10
    else:
        pip = int(card)

    return pip

def higher_card(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    max = 0 # max(較大者)

    if pip1 == pip2:
        max = (card_one, card_two)
    elif pip1 > pip2: 
        max = card_one
    else:
        max = card_two
        
    return max
    
def value_of_ace(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數) 
    pip_A = 0
    
    if pip1 < pip2:
        pip1, pip2 = pip2, pip1

    if pip2 == 1:
        pip2 = 11
        
    if pip1 + pip2 <= 10:
        pip_A = 11
    else:
        pip_A = 1

    return pip_A

def is_blackjack(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    pos_A = 0# position (A的位置)
    blackjack  = False# 是否為21點

    if pip1 + pip2 == 11 and (pip1 == 10 or pip2 == 10):
        if pip1 == 1:
            pos_A = 0
        else:
            pos_A = 1
        blackjack = True
    else:
        blackjack = False

    return blackjack

def can_split_pairs(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    split_pairs = False

    if pip1 == pip2:
        split_pairs = True

    return split_pairs

def can_double_down(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    double_down_list = [9, 10, 11]
    can_double = False
    
    if pip1 + pip2 in double_down_list:
        can_double = True

    return can_double
