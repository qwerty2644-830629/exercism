"""Functions for tracking poker hands and assorted card tasks."""

def get_rounds(number):
    # number current number (當前的號碼)

    number_list = [number, number + 1, number + 2]

    return number_list

def concatenate_rounds(rounds_1, rounds_2):
    # round_1 first rounds number (第一局數字) 
    # round_2 scend rounds number (第二局數字)
    
    return rounds_1 + rounds_2
    
def list_contains_round(rounds, number):
    # round all round number (整回合的數字) 
    # number target number (目標數字)

    return number in rounds

def card_average(hand):
    # card in hand (手牌)    
    num_card  = len(hand) # number of card (牌數)

    return sum(hand) / num_card

def approx_average_is_average(hand):
    # card in hand (手牌)    
    num_card  = len(hand) # number of card (牌數)    
    modth1  = (hand[0] + hand[-1]) / 2 # first and end average (第一個和最後一個數字的平均值)
    modth2 = hand[int(num_card/2)] # 'middle' card (手牌的中位數)
    average = card_average(hand)
    
    return  modth1 == average or modth2 == average

def average_even_is_average_odd(hand):
    even_list = hand[0:len(hand):2] # all even index(奇數索引)
    odd_list = hand[1:len(hand):2] # all odd index (偶數索引)
    even_average = card_average(even_list) # (奇數平均)
    odd_average = card_average(odd_list) #　（偶數平均）

    return even_average == odd_average

def maybe_double_last(hand):
    #　hand (手牌)

    # the least one caed is 'J' value mlutiple 2 (最後一張是 J 分乘2)
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2

    return hand