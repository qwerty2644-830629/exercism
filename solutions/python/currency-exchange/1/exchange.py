def exchange_money(budget, exchange_rate): 
    return budget / exchange_rate
    
    """
    budget(兌換金額)
    exchange_rate(匯率)
    
    return Currency exchange value(交換貨幣的價值)
    """
    
def get_change(budget, exchanging_value):
    return budget - exchanging_value
    
    """
    budget(兌換前金額)
    exchange_value(想要兌換的金額)
    
    return the leave money(剩餘的原始貨幣金額)
    """
    
def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills
    
    """
    denomination(鈔票面值)
    number_of_bills(鈔票數)
    
    return total value bills(總金額)
    """
    
def get_number_of_bills(amount, denomination):
    return (amount // denomination)
    """
    amount(總價值)
    denomination(鈔票面值)
    
    return bills number(鈔票數)
    """
    
def get_leftover_of_bills(amount, denomination):
    number_of_bills = get_number_of_bills(amount, denomination)
    return amount - (number_of_bills * denomination)
    
    """
    amount(總價值)
    denomination(鈔票面值)
    bills number(鈔票數)
    
    return 兌換後剩餘零錢
    """

def exchangeable_value(budget, exchange_rate, spread, denomination):
    amount = exchange_money(budget, exchange_rate * (1 + spread / 100))
    number_of_bills = get_number_of_bills(amount, denomination)
    return int(number_of_bills * denomination)
    
    """
    budget(兌換前金額)
    exchange_rate(匯率)
    spread(手續費百分比)
    denomination(鈔票面值)

    number_of_bills(鈔票數)
    amount(新貨幣總價值)
    """