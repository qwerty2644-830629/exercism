def resistor_label(colors):
    ohem_code = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
                 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    tolerance_code = {'grey': 0.05, 'violet': 0.1, 'blue': 0.25, 'green': 0.5,
                     'brown': 1, 'red': 2, 'gold': 5, 'silver': 10}
    value = 0
    metric = 'ohms'
    if len(colors) < 4: return '0 ohms'
    for i in range(len(colors) - 2):
        value += (10 ** (len(colors) - 3 - i)) * ohem_code[colors[i]]
        print(value, 10 ** (len(colors) - 3 - i), ohem_code[colors[i]])

    if  value * (10 ** ohem_code[colors[-2]]) >= 10 ** 9:
        value *=  (10 ** ohem_code[colors[-2]]) / 10 ** 9
        metric = 'gigaohms'
    elif value * (10 ** ohem_code[colors[-2]])  >= 10 ** 6:
        value *= (10 ** ohem_code[colors[-2]]) / 10 ** 6
        metric = 'megaohms'
    elif value * (10 ** ohem_code[colors[-2]]) >= 10 ** 3:
        value *= (10 ** ohem_code[colors[-2]]) / 10 ** 3
        metric = 'kiloohms'
    else: value *= 10 ** ohem_code[colors[-2]]

    if value % 1.0 == 0: value = int(value)

    print(value)
    
    return f'{str(round(value,2))} {metric} ±{tolerance_code[colors[-1]]}%'