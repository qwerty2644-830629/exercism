def value_of_card(card): # 計算牌的價值
    # card(牌的數字)
    pip = 0 # (點數)

    if card == "A": # A = 1
        pip = 1
    elif card == "J" or card == "Q" or card == "K": # J Q K 為 10
        pip = 10
    else:
        pip = int(card)

    return pip

def higher_card(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    max_pip = 0 # max(較大者)

    if pip1 == pip2:
        max_pip = (card_one, card_two)
    elif pip1 > pip2: 
        max_pip = card_one
    else:
        max_pip = card_two
        
    return max_pip
    
def value_of_ace(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數) 
    pip_a = 0 # (A的點數)
    
    if pip1 < pip2: # pip1(max) pip2(min)
        pip1, pip2 = pip2, pip1

    if pip2 == 1: # 最小的為A時 這個A = 11
        pip2 = 11
        
    if pip1 + pip2 <= 10: # 三張總和 < 21
        pip_a = 11
    else:
        pip_a = 1

    return pip_a

def is_blackjack(card_one, card_two):
    # card_one(第一張牌) card_two(第二張牌)
    pip1 = value_of_card(card_one)# (第一張點數)
    pip2 = value_of_card(card_two)# (第二張點數)
    pos_A = 0# position (A的位置)
    blackjack  = False# 是否為21點

    if pip1 + pip2 == 11 and (pip1 == 10 or pip2 == 10): # 其中一張為 10 且 另一張為 A
        if pip1 == 1: # 哪張為 A
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
